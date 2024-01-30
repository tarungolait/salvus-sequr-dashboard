import React from 'react';

const Barcode = () => {
  // Function to handle printing
  const handlePrint = () => {
    window.print();
  };

  
    return (
      <div className="m-4 md:m-10 mt-24 p-10 bg-white dark:bg-secondary-dark-bg rounded-3xl">
        <h2 className="text-lg font-bold mb-4">Product Details</h2>
        <div className="overflow-x-auto">
          <form className="w-full max-w-lg">
            <table className="w-full">
              <tbody>
                <tr>
                  <td className="px-3 py-2">
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="ble-mac-id">
                      BLE MAC ID
                    </label>
                    <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="ble-mac-id" type="text" placeholder="Enter BLE MAC ID" />
                  </td>
                  <td className="px-3 py-2">
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="product-type">
                      PRODUCT TYPE
                    </label>
                    <select className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="product-type">
                      <option>Select type</option>
                      {/* Add options for product types here */}
                    </select>
                  </td>
                </tr>
                <tr>
                  <td className="px-3 py-2">
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="wallet-color">
                      WALLET COLOR
                    </label>
                    <select className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="wallet-color">
                      <option>Select color</option>
                      {/* Add options for wallet colors here */}
                    </select>
                  </td>
                  <td className="px-3 py-2">
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="batch-number">
                      BATCH NUMBER
                    </label>
                    <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="batch-number" type="text" placeholder="Enter batch number" />
                  </td>
                </tr>
                <tr>
                  <td className="px-3 py-2">
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="qr-code">
                      QR CODE
                    </label>
                    <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="qr-code" type="text" placeholder="Enter QR code" />
                  </td>
                  <td className="px-3 py-2">
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="barcode-number">
                      BARCODE NO
                    </label>
                    <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="barcode-number" type="text" placeholder="Enter barcode number" />
                  </td>
                </tr>
                <tr>
                  <td className="px-3 py-2">
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="version">
                      VERSION
                    </label>
                    <select className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="version">
                      <option>Select version</option>
                      {/* Add options for versions here */}
                    </select>
                  </td>
                  <td className="px-3 py-2">
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="delete-mac-id">
                      ENTER MAC ID TO DELETE
                    </label>
                    <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="delete-mac-id" type="text" placeholder="Enter MAC ID to delete" />
                  </td>
                </tr>
              </tbody>
            </table>
            <div className="flex justify-center mt-8"> {/* Adjusted wrapper for buttons */}
            <button className="shadow bg-blue-500 hover:bg-blue-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="submit">
              Submit
            </button>
            {/* Add a button for printing */}
            <button className="shadow bg-gray-500 hover:bg-gray-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded ml-4" onClick={handlePrint}>
              Print
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
  
export default Barcode;
