import React, { useState } from 'react';
import axios from 'axios'; // Import Axios for making HTTP requests

const NewProduct = () => {
  // State variables to hold form input values
  const [productCategory, setProductCategory] = useState('');
  const [productType, setProductType] = useState('');
  const [color, setColor] = useState('');
  const [batteryType, setBatteryType] = useState('');
  const [bleMake, setBleMake] = useState('');
  const [version, setVersion] = useState('');

  // Function to handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    // Create an object with form data
    const formData = {
      product_category: productCategory,
      product_type: productType,
      color: color,
      battery_type: batteryType,
      ble_make: bleMake,
      version: version
    };

    try {
      // Make a POST request to the backend endpoint
      const response = await axios.post('http://localhost:5000/api/product-details', formData);
      console.log(response.data); // Log the response from the backend
      // Clear form fields after successful submission (optional)
      setProductCategory('');
      setProductType('');
      setColor('');
      setBatteryType('');
      setBleMake('');
      setVersion('');
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  return (
    <div className="m-4 md:m-10 mt-24 p-10 bg-white dark:bg-secondary-dark-bg rounded-3xl">
      <h2 className="text-lg font-bold mb-4">New Product</h2>
      <div className="overflow-x-auto">
        <form className="w-full max-w-lg" onSubmit={handleSubmit}>
          <table className="w-full">
            <tbody>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="product-category">
                    Product Category
                  </label>
                  <input 
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" 
                    id="product-category" 
                    type="text" 
                    placeholder="Enter product category" 
                    value={productCategory}
                    onChange={(e) => setProductCategory(e.target.value)}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="product-type">
                    Product Type
                  </label>
                  <input 
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" 
                    id="product-type" 
                    type="text" 
                    placeholder="Enter product type" 
                    value={productType}
                    onChange={(e) => setProductType(e.target.value)}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="color">
                    Color
                  </label>
                  <input 
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" 
                    id="color" 
                    type="text" 
                    placeholder="Enter color" 
                    value={color}
                    onChange={(e) => setColor(e.target.value)}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="battery-type">
                    Battery Type
                  </label>
                  <input 
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" 
                    id="battery-type" 
                    type="text" 
                    placeholder="Enter battery type" 
                    value={batteryType}
                    onChange={(e) => setBatteryType(e.target.value)}
                  />
                </td>
              </tr>
              <tr>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="ble-make">
                    BLE Make
                  </label>
                  <input 
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" 
                    id="ble-make" 
                    type="text" 
                    placeholder="Enter BLE make" 
                    value={bleMake}
                    onChange={(e) => setBleMake(e.target.value)}
                  />
                </td>
                <td className="px-3 py-2">
                  <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="version">
                    Version
                  </label>
                  <input 
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" 
                    id="version" 
                    type="text" 
                    placeholder="Enter version" 
                    value={version}
                    onChange={(e) => setVersion(e.target.value)}
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
        </form>
      </div>
    </div>
  );
};

export default NewProduct;
