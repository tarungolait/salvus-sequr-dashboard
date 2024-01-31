import React, { useState } from 'react';

const Barcode = () => {
  const [formData, setFormData] = useState({
    blemacid: '',
    wallet_type: '',
    walletcolor: '',
    manufacturingdate: new Date().toISOString().split("T")[0], // Initializing with current date
    batchnum: '012003202102',
    countrycode: '890',
    qrcode: '',
    barcodeno: '',
    version: '',
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
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="blemacid">
                    Category
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="blemacid"
                    type="text"
                    placeholder="Select"
                    name="blemacid"
                    value={formData.blemacid}
                    onChange={handleChange}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="wallet_type">
                    Type
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="wallet_type"
                    type="text"
                    placeholder="Select Product Type"
                    name="wallet_type"
                    value={formData.wallet_type}
                    onChange={handleChange}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="walletcolor">
                    Color
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="walletcolor"
                    type="text"
                    placeholder="Select Color"
                    name="walletcolor"
                    value={formData.walletcolor}
                    onChange={handleChange}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="manufacturingdate">
                    MAC ID
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="manufacturingdate"
                    type="text"
                    placeholder="Enter MacID"
                    name="manufacturingdate"
                    value={formData.manufacturingdate}
                    onChange={handleChange}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="qrcode">
                    QR Code
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="qrcode"
                    type="text"
                    placeholder="Enter QR Code"
                    name="qrcode"
                    value={formData.qrcode}
                    onChange={handleChange}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="barcodeno">
                    Barcode No
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="barcodeno"
                    type="text"
                    placeholder="Enter Barcode No"
                    name="barcodeno"
                    value={formData.barcodeno}
                    onChange={handleChange}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="version">
                    Version
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
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="batchnum">
                    Batch Number
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="batchnum"
                    type="text"
                    placeholder="Enter Batch Number"
                    name="batchnum"
                    value={formData.batchnum}
                    onChange={handleChange}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="countrycode">
                    Country Code
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="countrycode"
                    type="text"
                    placeholder="Enter Country Code"
                    name="countrycode"
                    value={formData.countrycode}
                    onChange={handleChange}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="manufacturingdate">
                    Manufacturing Date
                  </label>
                  <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="manufacturingdate"
                    type="text"
                    placeholder="Enter MacID"
                    name="manufacturingdate"
                    value={formData.manufacturingdate}
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
