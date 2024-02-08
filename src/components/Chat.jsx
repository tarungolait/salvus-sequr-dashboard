import React, { useState } from 'react';
import { MdOutlineSearch, MdOutlineCancel } from 'react-icons/md';
import { Button } from '.';
import { useStateContext } from '../contexts/ContextProvider';

const Chat = () => {
  const { currentColor } = useStateContext();
  const [searchInput, setSearchInput] = useState('');
  const [searchResult, setSearchResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    try {
      const response = await fetch(`http://localhost:5000/api/data-entry/search`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          qrCode: searchInput,
          barcodeNo: searchInput,
          macId: searchInput
        })
      });
      if (!response.ok) {
        throw new Error('Failed to fetch search results');
      }
      const data = await response.json();
      if (data.error) {
        throw new Error(data.error);
      }
      setSearchResult(data);
      setError(null);
    } catch (error) {
      console.error('Error searching data:', error.message);
      setSearchResult(null);
      setError(error.message);
    }
  };

      const handlePrintBarcode = () => {
        if (searchResult && searchResult.barcodeLocation) {
            const barcodeImage = new Image();
            barcodeImage.src = searchResult.barcodeLocation;
            barcodeImage.onload = () => {
                const printWindow = window.open('', '_blank');
                if (printWindow) {
                    printWindow.document.write('<html><head><title>Print Barcode</title></head><body>');
                    printWindow.document.write('<div style="text-align:center;">Loading Barcode...</div>');
                    printWindow.document.write('</body></html>');
                    printWindow.document.close();
                    setTimeout(() => {
                        printWindow.document.body.innerHTML = '';
                        printWindow.document.write('<html><head><title>Print Barcode</title></head><body>');
                        printWindow.document.write('<img src="' + barcodeImage.src + '" style="max-width:100%;height:auto;" />');
                        printWindow.document.write('</body></html>');
                        printWindow.document.close();
                        printWindow.print(); // Directly print the opened window
                    }, 1000); // Delay of 1 second (1000 milliseconds)
                } else {
                    console.error('Failed to open print window');
                }
            };
            barcodeImage.onerror = () => {
                console.error('Failed to load barcode image');
            };
        }
    };
    
    const handlePrintQRCode = () => {
      if (searchResult && searchResult.qrCodeLocation && searchResult.qrCode) {
          const qrCodeImage = new Image();
          qrCodeImage.src = searchResult.qrCodeLocation;
          qrCodeImage.onload = () => {
              const printWindow = window.open('', '_blank');
              if (printWindow) {
                  printWindow.document.write(`
                      <html>
                          <head>
                              <title>Print QR Code</title>
                              <style>
                                  .container {
                                      position: relative;
                                      width: calc(2.5cm - 2px);
                                      height: calc(2.5cm - 2px);
                                      background-color: #f0f0f0;
                                      border: 1px solid #ccc;
                                      display: flex;
                                      justify-content: center;
                                      align-items: center;
                                      padding: 8px;
                                  }
                                  
                                  img {
                                      max-width: 100%;
                                      max-height: 100%;
                                      width: 100%; 
                                      height: auto; 
                                  }
                                  
                                  .qr-code-number {
                                      position: absolute;
                                      bottom: -1px;
                                      left: 50%;
                                      transform: translateX(-50%);
                                      font-size: 10px;
                                      
                                  }
                              </style>
                          </head>
                          <body>
                              <div class="container">
                                  <img src="${qrCodeImage.src}" />
                                  <div class="qr-code-number">${searchResult.qrCode}</div>
                              </div>
                          </body>
                      </html>
                  `);
                  printWindow.document.close();
                  printWindow.print(); // Directly print the opened window
              } else {
                  console.error('Failed to open print window');
              }
          };
          qrCodeImage.onerror = () => {
              console.error('Failed to load QR code image');
          };
      }
  };
  
  
  
    

  return (
<div className="nav-item fixed left-0 right-0 top-0 bottom-0 bg-white dark:bg-[#42464D] p-8 rounded-lg h-screen">
  <div className="flex justify-between items-center">
    <div className="flex gap-3" style={{ position: "relative", left: "1100px", top: "/* specify top positioning */" }}>
      <div className="flex items-center gap-2">
        <input 
          type="text" 
          placeholder="Search..." 
          className="border-2 border-black rounded-md px-3 py-2" 
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        />
        <button 
          type="button" 
          className="bg-black text-white rounded-md p-2 hover:bg-gray-800" 
          onClick={handleSearch}
        >
          <MdOutlineSearch />
        </button>
      </div>
      <button type="button" className="text-white text-xs rounded p-1 px-2 bg-orange">
        Search
      </button>
    </div>
    <div style={{ position: "relative", top: "-30px", right: "-20px" }}>
  <Button
    icon={<MdOutlineCancel />}
    color="rgb(153, 171, 180)"
    bgHoverColor="light-gray"
    size="2xl"
    borderRadius="50%"
  />
</div>

      
      </div>
      {searchResult && (
        <div className="bg-gray-100 p-5 rounded-md" style={{ height: '500px', width: '80%', margin: '0 auto', position: 'relative', top: '50px', left: '50px' }}>
        <h3 className="font-semibold mb-2 ml-10 mt-10">Search Result</h3>

    <div className="grid grid-cols-2 gap-4">
         <ul className="ml-10 mt-10">
              <li><strong>Category:</strong> {searchResult.category}</li>
              <li><strong>Type:</strong> {searchResult.type}</li>
              <li><strong>Color:</strong> {searchResult.color}</li>
              <li><strong>MAC ID:</strong> {searchResult.macId}</li>
              <li><strong>QR Code:</strong> {searchResult.qrCode}</li>
              <li><strong>Barcode No:</strong> {searchResult.barcodeNo}</li>
              <li><strong>Version:</strong> {searchResult.version}</li>
              <li><strong>Batch Number:</strong> {searchResult.batchNumber}</li>
              <li><strong>Country Code:</strong> {searchResult.countryCode}</li>
              <li><strong>Manufacturing Date:</strong> {searchResult.manufacturingDate && new Date(searchResult.manufacturingDate).toLocaleDateString('en-GB')}</li>
            </ul>
            <div className="flex justify-center items-center flex-col">
              {searchResult.barcodeLocation && (
                <div className="mb-4 position-relative">
                  <img src={searchResult.barcodeLocation} alt="Barcode" style={{ maxWidth: "100%", height: "auto", position: "relative", top: "-10px", right: "300px" }} />
                  <button
                    onClick={handlePrintBarcode}
                    className="shadow bg-blue-500 hover:bg-blue-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-3 rounded mt-2"
                    type="button"
                    style={{ position: "absolute", top: "250px", right: "530px" }}
                  >
                    Print Barcode
                  </button>
                </div>
              )}
              {searchResult.qrCodeLocation && (
                <div className="mb-4 position-relative">
                  <img src={searchResult.qrCodeLocation} alt="QR Code" style={{ maxWidth: "33%", height: "auto", position: "relative", top: "-120px", right: "-60px" }} />
                  <button
                    onClick={handlePrintQRCode}
                    className="shadow bg-blue-500 hover:bg-blue-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-3 rounded mt-2"
                    type="button"
                    style={{ position: "absolute", top: "250px", right: "280px" }}
                  >
                    Print QR Code
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chat;
