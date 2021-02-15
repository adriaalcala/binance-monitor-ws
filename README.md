## BINANCE SYMBOL MONITOR
Monitor the market data and print out every time the price goes above the input number

## Usage
The usage of this tool it's very simple, just build the Docker image and run it.
`docker build -t binance .`
`docker run --rm -it binance {symbol} {min_price}`

This will output all the data obtained from symbol.


## How to add more steps to pipeline
Just create a processor inside `pipeline` module and add it to processors lists in `pipeline.main`
