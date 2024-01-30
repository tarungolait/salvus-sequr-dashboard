import React from 'react';

const Delete = () => {
  
    return (
      <div className="m-4 md:m-10 mt-24 p-10 bg-white dark:bg-secondary-dark-bg rounded-3xl">
        <h2 className="text-lg font-bold mb-4">Device Details</h2>
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
                    <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="qr-code-ref">
                      QR CODE REF NO.
                    </label>
                    <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="qr-code-ref" type="text" placeholder="Enter QR code reference number" />
                  </td>
                  <td className="px-3 py-2">
                    {/* Adjusted button container */}
                    <div className="mt-7">
                      <button className="shadow bg-red-500 hover:bg-red-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="button">
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </form>
        </div>
      </div>
    );
  };
export default Delete;
