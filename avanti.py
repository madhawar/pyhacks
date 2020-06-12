import webbrowser

voucher = input("Enter Voucher Code: ")
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#webbrowser.open('https://qa09avn.intertrav.co.uk/travelinsurance/quote/applyVoucher?voucherCode=' + voucher)
webbrowser.get(chrome_path).open('https://qa09avn.intertrav.co.uk/travelinsurance/quote/applyVoucher?voucherCode=' + voucher)