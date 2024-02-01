import React, { useState } from 'react';
import axios from 'axios';

const Bankcontacts = () => {
  const [formData, setFormData] = useState({
    bankName: '',
    typeOfBank: '',
    address: '',
    city: '',
    country: '',
    customerCareNumber: '',
    emailId: '',
    officialWebsite: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:5000/api/bankcontacts', formData);
      // Optionally clear form fields after successful submission
      setFormData({
        bankName: '',
        typeOfBank: '',
        address: '',
        city: '',
        country: '',
        customerCareNumber: '',
        emailId: '',
        officialWebsite: ''
      });
      console.log('Data submitted successfully'); // Log success message to console
  } catch (error) {
    console.error('Error submitting data:', error);
    alert('Error submitting data. Please try again.');
  }
};

  return (
    <div className="m-4 md:m-10 mt-24 p-10 bg-white dark:bg-secondary-dark-bg rounded-3xl">
      <h2 className="text-lg font-bold mb-4">Contact Details of Banks</h2>
      <div className="overflow-x-auto">
        <form className="w-full max-w-lg" onSubmit={handleSubmit}>
          <table className="w-full">
            <tbody>
              <tr>
                <td className="px-3 py-2">
                  <label htmlFor="bank-name" className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">BANK NAME</label>
                  <input type="text" id="bank-name" name="bankName" value={formData.bankName} onChange={handleChange} placeholder="Enter bank name" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" />
                </td>
                <td className="px-3 py-2">
                  <label htmlFor="type-of-bank" className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">TYPE OF BANK</label>
                  <input type="text" id="type-of-bank" name="typeOfBank" value={formData.typeOfBank} onChange={handleChange} placeholder="Enter type of bank" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label htmlFor="address" className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">ADDRESS</label>
                  <input type="text" id="address" name="address" value={formData.address} onChange={handleChange} placeholder="Enter address" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" />
                </td>
                <td className="px-3 py-2">
                  <label htmlFor="city" className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">CITY</label>
                  <input type="text" id="city" name="city" value={formData.city} onChange={handleChange} placeholder="Enter city" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label htmlFor="country" className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">COUNTRY</label>
                  <input type="text" id="country" name="country" value={formData.country} onChange={handleChange} placeholder="Enter country" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" />
                </td>
                <td className="px-3 py-2">
                  <label htmlFor="customer-care-number" className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">CUSTOMER CARE NUMBER</label>
                  <input type="text" id="customer-care-number" name="customerCareNumber" value={formData.customerCareNumber} onChange={handleChange} placeholder="Enter customer care number" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label htmlFor="email-id" className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">EMAIL ID</label>
                  <input type="email" id="email-id" name="emailId" value={formData.emailId} onChange={handleChange} placeholder="Enter email ID" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" />
                </td>
                <td className="px-3 py-2">
                  <label htmlFor="official-website" className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">OFFICIAL WEBSITE OF THE BANK</label>
                  <input type="text" id="official-website" name="officialWebsite" value={formData.officialWebsite} onChange={handleChange} placeholder="Enter official website" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" />
                </td>
              </tr>
            </tbody>
          </table>
          <div className="flex justify-center mt-8">
            <button type="submit" className="shadow bg-blue-500 hover:bg-blue-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded">Submit</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Bankcontacts;
