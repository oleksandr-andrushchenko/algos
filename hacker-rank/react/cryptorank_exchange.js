import React, {useState, useEffect} from "react"

export const cryptocurrencyList = [
  {
    code: "BNB",
    name: "BNB",
    rate: 0.00311839
  },
  {
    code: "BTC",
    name: "Bitcoin",
    rate: 0.00004066
  },
  {
    code: "DOGE",
    name: "Dogecoin",
    rate: 11.18558722
  },
  {
    code: "ETH",
    name: "Ethereum",
    rate: 0.00059237
  },
  {
    code: "XRP",
    name: "XRP",
    rate: 2.50682634
  }
]

function Table({amount}) {
  return (
    <div className="card card-text mt-10 mx-4">
      <table className="mb-0">
        <thead>
        <tr>
          <th>Cryptocurrency</th>
          <th>Exchange Rate</th>
          <th>Number of Coins</th>
        </tr>
        </thead>
        <tbody data-testid="exchange-data">
        {cryptocurrencyList.map((crypto, index) => (
          <tr key={index}>
            <td>{crypto.name}</td>
            <td>1 USD = {crypto.rate} {crypto.code}</td>
            <td>{isNaN(amount) ? "n/a" : (amount * crypto.rate).toFixed(8)}</td>
          </tr>
        ))}
        </tbody>
      </table>
    </div>
  )
}

function Main() {
  const [error, setError] = useState("")
  const [balance, setBalance] = useState(17042.67)
  const [amount, setAmount] = useState(null)

  useEffect(() => {
    if (amount === null) {
      return
    }
    if (amount === "") {
      setError("Amount cannot be empty")
    } else if (amount < 0.01) {
      setError("Amount cannot be less than $0.01")
    } else if (amount > balance) {
      setError("Amount cannot exceed the available balance")
    }
  }, [amount, balance])

  return (
    <div className="layout-column align-items-center mx-auto">
      <h1>CryptoRank Exchange</h1>
      <section>
        <div className="card-text layout-column align-items-center mt-12 px-8 flex text-center">
          <label>
            I want to exchange $ <input className="w-10" data-testid="amount-input" required type="number"
                                        placeholder="USD" value={amount}
                                        onChange={(e) => setAmount(e.target.value)}/> of my $
            <span>{balance}</span>:
          </label>
          {error && (
            <p data-testid="error" className="form-hint error-text mt-3 pl-0 ml-0">{error}</p>
          )}
          {/* The errors can be Amount cannot be empty /be less than $0.01/exceed the available balance */}
        </div>
      </section>
      <Table amount={error ? "qweqwe" : amount}/>
    </div>
  )
}

export default Main

