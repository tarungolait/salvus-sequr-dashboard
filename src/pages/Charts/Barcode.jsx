import React, { useState } from 'react';

const Barcode = () => {
  const [formData, setFormData] = useState({
    category: '',
    type: '',
    color: '',
    macId: '',
    qrCode: '',
    barcodeNo: '',
    version: '',
    batchNumber: '012003202102', // Constant value for batchNumber
    countryCode: '890', // Constant value for countryCode
    manufacturingDate: new Date().toISOString().split("T")[0], // Initializing with current date
  });

  const [notification, setNotification] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/api/data-entry', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      console.log(data);
      // Handle success or display feedback to the user
      showNotification('Form submitted successfully', 'success');
    } catch (error) {
      console.error('Error:', error);
      // Handle error or display feedback to the user
      showNotification('Error submitting form', 'error');
    }
  };

  const showNotification = (message, type = 'success') => {
    setNotification({ message, type });
    setTimeout(() => {
      setNotification(null);
    }, 3000);
  };

  return (
    <div className="m-4 md:m-10 mt-24 p-10 bg-white dark:bg-secondary-dark-bg rounded-3xl">
      <h2 className="text-lg font-bold mb-4">Product Details</h2>
      <div className="overflow-x-auto">
        <form className="w-full max-w-lg" onSubmit={handleSubmit}>
          <table className="w-full">
            <tbody>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="category">
                    CATEGORY
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="category"
                    type="text"
                    placeholder="Enter Category"
                    name="category"
                    value={formData.category}
                    onChange={handleChange}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="type">
                    TYPE
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="type"
                    type="text"
                    placeholder="Enter Type"
                    name="type"
                    value={formData.type}
                    onChange={handleChange}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="color">
                    COLOR
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="color"
                    type="text"
                    placeholder="Enter Color"
                    name="color"
                    value={formData.color}
                    onChange={handleChange}
                  />
                </td>
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
              </tr>
              <tr>
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
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="version">
                    VERSION
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="version"
                    type="text"
                    placeholder="Enter Version"
                    name="version"
                    value={formData.version}
                    onChange={handleChange}
                  />
                </td>
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
              </tr>
              <tr>
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
            </tbody>
          </table>
          <div className="flex justify-center mt-8">
            <button className="shadow bg-blue-500 hover:bg-blue-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="submit">
              Submit
            </button>
          </div>
          {notification && (
            <div className={`notification ${notification.type}`}>
              {notification.message}
            </div>
          )}
        </form>
      </div>
    </div>
  );
};

export default Barcode;
