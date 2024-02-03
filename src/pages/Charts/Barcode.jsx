import React, { useState, useEffect } from 'react';

const Barcode = () => {
  const [formData, setFormData] = useState({
    category: '',
    type: '',
    color: '',
    macId: '',
    qrCode: '',
    barcodeNo: '',
    version: '',
    batchNumber: '012003202102',
    countryCode: '890',
    manufacturingDate: new Date().toISOString().split("T")[0],
  });
  const [barcodeUrl, setBarcodeUrl] = useState('');
  const [qrCodeUrl, setQrCodeUrl] = useState('');
  const [notification, setNotification] = useState(null);
  const [categories, setCategories] = useState([]);
  const [types, setTypes] = useState([]);
  const [colors, setColors] = useState([]);
  const [versions, setVersions] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      // Fetch product details including categories, types, colors, and versions
      const response = await fetch('http://localhost:5000/api/product-details');
      const data = await response.json();
      const { categories, types, colors, versions } = data;
      setCategories(categories);
      setTypes(types);
      setColors(colors);
      setVersions(versions);
  
      // Fetch latest barcode number and QR code
      const productCodesResponse = await fetch('http://localhost:5000/api/product-codes');
      const productCodesData = await productCodesResponse.json();
  
      // Increment the barcode number and QR code by 1
      const nextBarcodeNo = parseInt(productCodesData.barcodeNo) + 1;
      const nextQrCode = (parseInt(productCodesData.qrCode) + 1).toString().padStart(productCodesData.qrCode.length, '0');
  
      // Update the formData state with incremented barcodeNo and qrCode
      setFormData({
        ...formData,
        qrCode: nextQrCode,
        barcodeNo: nextBarcodeNo.toString()
      });
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });

    // Regular expression to validate BLE MAC ID format
    const macIdRegex = /^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$/;

    // Check if the input value matches the MAC ID format
    const isValidMacId = macIdRegex.test(value);

    // Show an error notification if the input value is not a valid MAC ID
    if (name === 'macId' && !isValidMacId && value !== '') {
      showNotification('Invalid BLE MAC ID format', 'error');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const isAnyFieldEmpty = Object.values(formData).some(value => value === '');
    if (isAnyFieldEmpty) {
      showNotification('All fields are required', 'error');
      return;
    }

    try {
      // Check if MAC ID, Barcode, and QR Code already exist in the data_entry table
      const checkDuplicateResponse = await fetch(`http://localhost:5000/api/data-entry/check-duplicate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          macId: formData.macId,
          barcodeNo: formData.barcodeNo,
          qrCode: formData.qrCode
        }),
      });

      const checkDuplicateData = await checkDuplicateResponse.json();
      
      if (checkDuplicateData.duplicateFound) {
        showNotification('Duplicate entry found for MAC ID, Barcode, or QR Code', 'error');
        return;
      }

      // Proceed with form submission if no duplicate entry found
      const response = await fetch(`http://localhost:5000/api/product-codes?increment_on_submit=true`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      const productCodesData = await response.json();
      console.log(productCodesData);

      const data = {
        ...formData,
        qrCode: productCodesData.qrCode,
        barcodeNo: productCodesData.barcodeNo
      };

      const entryResponse = await fetch('http://localhost:5000/api/data-entry', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const entryData = await entryResponse.json();
      console.log(entryData);

      setBarcodeUrl(entryData.barcode_url);
      setQrCodeUrl(entryData.qrcode_url);

      showNotification('Form submitted successfully', 'success');
    } catch (error) {
      console.error('Error:', error);
      showNotification('Error submitting form', 'error');
    }
  };

  const showNotification = (message, type = 'success') => {
    setNotification({ message, type });
    setTimeout(() => {
      setNotification(null);
    }, 3000);
  };

  const handlePrintQRCode = () => {
    const qrCodeWindow = window.open('', '_blank');
    qrCodeWindow.document.write(
      `<img src="${qrCodeUrl}" style="width: 3cm; height: 3cm;" onload="window.print()" />`
    );
    qrCodeWindow.document.close();
  };

  const handlePrintBarcode = () => {
    const barcodeWindow = window.open('', '_blank');
    barcodeWindow.document.write(
      `<img src="${barcodeUrl}" style="width: 5cm; height: 2.5cm;" onload="window.print()" />`
    );
    barcodeWindow.document.close();
  };
  return (
    <div className="flex m-4 md:m-10 mt-24 p-10 bg-white dark:bg-secondary-dark-bg rounded-3xl">
      <div className="w-full max-w-lg">
        <h2 className="text-lg font-bold mb-4">Product Details</h2>
        <form onSubmit={handleSubmit}>
          <table className="w-full">
            <tbody>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="category">
                    CATEGORY
                  </label>
                  <select
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="category"
                    name="category"
                    value={formData.category}
                    onChange={handleChange}
                  >
                    <option value="">Select Category</option>
                    {categories.map(category => (
                      <option key={category} value={category}>{category}</option>
                    ))}
                  </select>
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="type">
                    TYPE
                  </label>
                  <select
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="type"
                    name="type"
                    value={formData.type}
                    onChange={handleChange}
                  >
                    <option value="">Select Type</option>
                    {types.map(type => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                  </select>
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="color">
                    COLOR
                  </label>
                  <select
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="color"
                    name="color"
                    value={formData.color}
                    onChange={handleChange}
                  >
                    <option value="">Select Color</option>
                    {colors.map(color => (
                      <option key={color} value={color}>{color}</option>
                    ))}
                  </select>
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="version">
                    VERSION
                  </label>
                  <select
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="version"
                    name="version"
                    value={formData.version}
                    onChange={handleChange}
                  >
                    <option value="">Select Version</option>
                    {versions.map(version => (
                      <option key={version} value={version}>{version}</option>
                    ))}
                  </select>
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="macId">
                    MAC ID
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="macId"
                    type="text"
                    placeholder="Enter Mac ID"
                    name="macId"
                    value={formData.macId}
                    onChange={handleChange}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="qrCode">
                    QR CODE
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="qrCode"
                    type="text"
                    placeholder="Enter QR Code"
                    name="qrCode"
                    value={formData.qrCode}
                    onChange={handleChange}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="barcodeNo">
                    BARCODE NO
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="barcodeNo"
                    type="text"
                    placeholder="Enter Barcode No"
                    name="barcodeNo"
                    value={formData.barcodeNo}
                    onChange={handleChange}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="manufacturingDate">
                    MANUFACTURING DATE
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="manufacturingDate"
                    type="text"
                    placeholder="Enter Manufacturing Date"
                    name="manufacturingDate"
                    value={formData.manufacturingDate}
                    onChange={handleChange}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="batchNumber">
                    BATCH NUMBER
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="batchNumber"
                    type="text"
                    placeholder="Enter Batch Number"
                    name="batchNumber"
                    value={formData.batchNumber}
                    onChange={handleChange}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="countryCode">
                    COUNTRY CODE
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="countryCode"
                    type="text"
                    placeholder="Enter Country Code"
                    name="countryCode"
                    value={formData.countryCode}
                    onChange={handleChange}
                  />
                </td>
              </tr>
            </tbody>
          </table>
          <div className="flex justify-center mt-8">
            <button className="shadow bg-blue-500 hover:bg-blue-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="submit">
              Submit
            </button>
            {qrCodeUrl && (
              <button className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 rounded ml-4" onClick={handlePrintQRCode}>Print QR Code</button>
            )}
            {barcodeUrl && (
              <button className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 rounded ml-4" onClick={handlePrintBarcode}>Print Barcode</button>
            )}
          </div>
          {notification && (
            <div className={`notification ${notification.type}`}>
              {notification.message}
            </div>
          )}
        </form>
      </div>
      {qrCodeUrl && (
        <div className="flex flex-col items-center ml-8 mt-8" style={{ marginLeft: '80px', marginTop: '190px' }}>
          <div style={{ backgroundColor: '#f5f5f5', marginBottom: '16px', borderRadius: '8px', border: '3px solid rgba(0, 0, 0, 0.5)' }}>
            <img src={qrCodeUrl} alt="QR Code" style={{ width: '120px', height: '120px', display: 'block', margin: '0 auto' }} />
          </div>
        </div>
      )}

      {barcodeUrl && (
        <div className="flex flex-col items-center ml-8 mt-8" style={{ marginLeft: '50px', marginTop: '210px' }}>
          <div style={{ backgroundColor: '#f5f5f5', borderRadius: '8px' }}>
            <img src={barcodeUrl} alt="Barcode" style={{ width: '150px', height: '80px', display: 'block', margin: '0 auto', border: '2px solid rgba(0, 0, 0, 0.5)' }} />
          </div>
        </div>
      )}
    </div>
  );
};

export default Barcode;
