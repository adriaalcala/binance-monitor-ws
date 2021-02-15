"""Binance monitor main module."""
from argparse import ArgumentParser

from binance_monitor.consumer import monitor_symbol


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("symbol", type=str, help="Symbol to monitor")
    parser.add_argument("min_price", type=float, help="Minimum price to monitor")
    args = parser.parse_args()
    monitor_symbol(args.symbol, args.min_price)
