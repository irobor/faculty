//  Meta.Mask В январе 2021 года  внесли ряд критических изменений в API нашего провайдера
// и удалили наш внедренный window.web3. 
// Эти изменения действуют на всех платформах начиная с версии: 9.0.2 of the MetaMask browser extension
//--
//На сегодняшний день MetaMask прекратил внедрение window.web3
//и внес ограниченное количество критических изменений в наш API-интерфейс поставщика Ethereum (window.ethereum).
// ЭТО КАСАЕТСЯ АККАУНТА И ТРАНЗАКЦИИ. В остальном можно работать с web3.js


if (typeof window.ethereum !== 'undefined') {
  console.log('MetaMask is installed!');  
}

	
	if(window.ethereum){
    window.web3 = new Web3(ethereum);
	try{
    window.ethereum.enable();
 
 

    
    const address = "0x048f756268f8aC8BFADd37C9eDb08788E6911D4B";
    var myContractInstance =  new web3.eth.Contract(abi, address);

  
  // API 0.2 использование window.ethereum для получения аккаунта от Мета Маски
  async function eventLog() {
      try {
       // API 0.2 использование window.ethereum для получения аккаунта от Мета Маски   
       const logg =  await ethereum.request({ method: 'eth_requestAccounts' });

       // web3.js 1.3.4
       const logEvent =  await   myContractInstance.events.Log(
        {
            filter: {sender:logg[0]}, // Using an array means OR: e.g. 20 or 23
            fromBlock: 0
        }, function(error, event){
            console.log('Await **',event['returnValues']['message']);
        });        
        return true ;
        
      } catch (error) {
          console.log(error);
      }
    
  }

  eventLog().then((result)=>{console.log('AWAIT', result);})





    // Получение аккунта метамаск, можно использовать в асинхронных запросах
    var acc = web3.eth.getAccounts(function(error, result){
        if (error) {
            console.log("Ошибка Аккаунта", error);
        }
        // console.log это вывод в элемент HTML
      console.log("Аккаунт", result[0]);
      return result[0] ;
      
     })
     // Получение аккаунта метааск, API 0.2 (работает)
     //const accountAPI = await ethereum.request({ method: 'eth_requestAccounts' });

   //web3 1.3.4
   // Выводит отдельно каждое событие
   var myEvent  =   myContractInstance.events.Log(
    {
        filter: {sender: "0x25221EAa9f95E9AF27CE567fC5248E9317F3F1C1"}, // Using an array means OR: e.g. 20 or 23
        fromBlock: 0
    },function(error, event){ console.log('событие - ',event['returnValues']['message']); });
  
   // получить журнал логов моего события.web3 1.3.4
   // Выводит массив событий
    var myResults = myContractInstance.getPastEvents('Log',
    {filter: {sender: "0x25221EAa9f95E9AF27CE567fC5248E9317F3F1C1"},
    fromBlock: 0},
    function(error, logs){
            if (error) {
            console.log("Ошибка", error);
        }

      console.log("событие Log, получаешь массив", logs);

 })  

 // все события и журнал логов web3 1.3.4
    var events = myContractInstance.events.allEvents('Log',{sender: account[0],fromBlock: 0, toBlock: 'latest'});
    console.log(events);
    events.get(function(error, logs){ 
        
        if (error) {
                console.log("Ошибка", error);
              }
        
              console.log("Все логи", logs);
        
        });
        
	}catch (error){
		
		console.log('Ошибка', error)
		}	
	}


