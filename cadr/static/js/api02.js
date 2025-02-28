if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
  }



  async function getAccount() {
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    const account = accounts[0];
    showAccount.innerHTML = account;
  }




try {
    // Request account access if needed
    const accounts = await ethereum.send('eth_requestAccounts');
    // Accounts now exposed, use them
    ethereum.send('eth_sendTransaction', { from: accounts[0], /* ... */ })
} catch (error) {
    // User denied account access
}