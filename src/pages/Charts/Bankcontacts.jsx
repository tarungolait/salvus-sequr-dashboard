import React from 'react';

const Bankcontacts = () => {
  return (
    <div className="m-4 md:m-10 mt-24 p-10 bg-white dark:bg-secondary-dark-bg rounded-3xl">
      <h2 className="text-lg font-bold mb-4">Contact Details of Banks</h2>
      <div className="overflow-x-auto">
        <form className="w-full max-w-lg">
          <table className="w-full">
            <tbody>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="bank-name">
                    BANK NAME
                  </label>
                  <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="bank-name" type="text" placeholder="Enter bank name" />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="type-of-bank">
                    TYPE OF BANK
                  </label>
                  <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="type-of-bank" type="text" placeholder="Enter type of bank" />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="address">
                    ADDRESS
                  </label>
                  <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="address" type="text" placeholder="Enter address" />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="city">
                    CITY
                  </label>
                  <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="city" type="text" placeholder="Enter city" />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="country">
                    COUNTRY
                  </label>
                  <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="country" type="text" placeholder="Enter country" />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="customer-care-number">
                    CUSTOMER CARE NUMBER
                  </label>
                  <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="customer-care-number" type="text" placeholder="Enter customer care number" />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="email-id">
                    EMAIL ID
                  </label>
                  <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="email-id" type="email" placeholder="Enter email ID" />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="official-website">
                    OFFICIAL WEBSITE OF THE BANK
                  </label>
                  <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="official-website" type="text" placeholder="Enter official website" />
                </td>
              </tr>
            </tbody>
          </table>
          <div className="flex justify-center mt-8"> {/* Adjusted wrapper for buttons */}
            <button className="shadow bg-blue-500 hover:bg-blue-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="submit">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};


export default Bankcontacts;
