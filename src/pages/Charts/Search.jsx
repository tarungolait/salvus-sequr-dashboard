import React, { useState } from 'react';

const Search = () => {
    const [searchInput, setSearchInput] = useState('');
    const [searchResult, setSearchResult] = useState(null);
    const [error, setError] = useState(null);
    const [deleteInput, setDeleteInput] = useState('');

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
                    printWindow.document.write('<img src="' + barcodeImage.src + '" style="max-width:100%;height:auto;" />');
                    printWindow.document.write('</body></html>');
                    printWindow.document.close();
                    printWindow.print(); // Directly print the opened window
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
        if (searchResult && searchResult.qrCodeLocation) {
            const qrCodeImage = new Image();
            qrCodeImage.src = searchResult.qrCodeLocation;
            qrCodeImage.onload = () => {
                const printWindow = window.open('', '_blank');
                if (printWindow) {
                    printWindow.document.write('<html><head><title>Print QR Code</title></head><body>');
                    printWindow.document.write('<img src="' + qrCodeImage.src + '" style="max-width:100%;height:auto;" />');
                    printWindow.document.write('</body></html>');
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

    const handleDeleteRow = async () => {
        try {
            const response = await fetch(`http://localhost:5000/api/data-entry/delete`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    macId: deleteInput
                })
            });
            if (!response.ok) {
                throw new Error('Failed to delete row');
            }
            setSearchResult(null); // Clear search result after deletion
            setError(null);
            setDeleteInput(''); // Clear delete input field
        } catch (error) {
            console.error('Error deleting row:', error.message);
            setError(error.message);
        }
    };

    return (
        <div className="m-4 md:m-10 mt-24 p-10 bg-white dark:bg-secondary-dark-bg rounded-3xl">
            <div className="flex justify-between mb-4">
                <h2 className="text-lg font-bold mb-4">Search Details</h2>
                <div className="w-1/2 px-3 flex justify-end">
                    <div className="relative">
                        <input
                            className="block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-2 px-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                            id="search-by"
                            type="text"
                            placeholder="Search"
                            value={searchInput}
                            onChange={(e) => setSearchInput(e.target.value)}
                        />
                    </div>
                    <button
                        onClick={handleSearch}
                        className="shadow bg-blue-500 hover:bg-blue-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-3 rounded ml-4"
                        type="button"
                        style={{ width: "80px" }} // Adjust width as needed
                    >
                        Search
                    </button>
                </div>
            </div>
            {error && <div className="text-red-500">{error}</div>}
            {searchResult && (
                <div>
                    <div className="bg-gray-100 p-4 rounded-md">
                        <h3 className="font-semibold mb-2">Search Result</h3>
                        <div className="grid grid-cols-2 gap-4">
                            <ul>
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
                                            style={{ position: "absolute", top: "400px", right: "580px" }}
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
                                            style={{ position: "absolute", top: "400px", right: "330px" }}
                                        >
                                            Print QR Code
                                        </button>
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                    <div className="flex justify-between mb-4" style={{ marginTop: '30px' }}>
                        <input
                            className="block w-1/5 bg-gray-200 text-gray-700 border border-gray-200 rounded py-2 px-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500 ml-auto"
                            type="text"
                            placeholder="MAC ID"
                            value={deleteInput}
                            onChange={(e) => setDeleteInput(e.target.value)}
                        />
                        <button
                            onClick={handleDeleteRow}
                            className="shadow bg-red-500 hover:bg-red-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-3 rounded ml-4"
                            type="button"
                        >
                            Delete
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Search;