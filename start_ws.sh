#!/bin/bash
cd ~/coinbase_WS/logs

COMMAND1=(python ~/coinbase_WS/scripts/cbpro.py)
COMMAND2=(python ~/coinbase_WS/scripts/bitfinex_btc.py)
COMMAND3=(python ~/coinbase_WS/scripts/bitfinex_dash.py)
COMMAND4=(python ~/coinbase_WS/scripts/bitfinex_eos.py)
COMMAND5=(python ~/coinbase_WS/scripts/bitfinex_etc.py)
COMMAND6=(python ~/coinbase_WS/scripts/bitfinex_eth.py)
COMMAND7=(python ~/coinbase_WS/scripts/bitfinex_iota.py)
COMMAND8=(python ~/coinbase_WS/scripts/bitfinex_ltc.py)
COMMAND9=(python ~/coinbase_WS/scripts/bitfinex_xlm.py)
COMMAND10=(python ~/coinbase_WS/scripts/bitfinex_xmr.py)
COMMAND11=(python ~/coinbase_WS/scripts/bitfinex_xrp.py)
COMMAND12=(python ~/coinbase_WS/scripts/bitfinex_zrx.py)
COMMAND13=(python ~/coinbase_WS/scripts/binance.py)
COMMAND14=(python ~/coinbase_WS/scripts/okex_bch.py)
COMMAND15=(python ~/coinbase_WS/scripts/okex_btc.py)
COMMAND16=(python ~/coinbase_WS/scripts/okex_etc.py)
COMMAND17=(python ~/coinbase_WS/scripts/okex_eth.py)
COMMAND18=(python ~/coinbase_WS/scripts/okex_ltc.py)

touch COMMAND1_failed
touch COMMAND2_failed
touch COMMAND3_failed
touch COMMAND4_failed
touch COMMAND5_failed
touch COMMAND6_failed
touch COMMAND7_failed
touch COMMAND8_failed
touch COMMAND9_failed
touch COMMAND10_failed
touch COMMAND11_failed
touch COMMAND12_failed
touch COMMAND13_failed
touch COMMAND14_failed
touch COMMAND15_failed
touch COMMAND16_failed
touch COMMAND17_failed
touch COMMAND18_failed

while true

do

        if [ -e COMMAND1_failed ]

        then

                # (Re)start Command1

                rm -f COMMAND1_failed; ("${COMMAND1[@]}"; touch COMMAND1_failed)&

        fi

         if [ -e COMMAND2_failed ]

        then

                # (Re)start Command2

                rm -f COMMAND2_failed; ("${COMMAND2[@]}"; touch COMMAND2_failed)&

        fi
		
		if [ -e COMMAND3_failed ]

        then

                # (Re)start Command3

                rm -f COMMAND3_failed; ("${COMMAND3[@]}"; touch COMMAND3_failed)&

        fi
		
		if [ -e COMMAND4_failed ]

        then

                # (Re)start Command4

                rm -f COMMAND4_failed; ("${COMMAND4[@]}"; touch COMMAND4_failed)&

        fi
		
		if [ -e COMMAND5_failed ]

        then

                # (Re)start Command5

                rm -f COMMAND5_failed; ("${COMMAND5[@]}"; touch COMMAND5_failed)&

        fi
		
		if [ -e COMMAND6_failed ]

        then

                # (Re)start Command6

                rm -f COMMAND6_failed; ("${COMMAND6[@]}"; touch COMMAND6_failed)&

        fi
		
		if [ -e COMMAND7_failed ]

        then

                # (Re)start Command7

                rm -f COMMAND7_failed; ("${COMMAND7[@]}"; touch COMMAND7_failed)&

        fi
		
		if [ -e COMMAND8_failed ]

        then

                # (Re)start Command8

                rm -f COMMAND8_failed; ("${COMMAND8[@]}"; touch COMMAND8_failed)&

        fi
		
		if [ -e COMMAND9_failed ]

        then

                # (Re)start Command9

                rm -f COMMAND9_failed; ("${COMMAND9[@]}"; touch COMMAND9_failed)&

        fi
		
		if [ -e COMMAND10_failed ]

        then

                # (Re)start Command10

                rm -f COMMAND10_failed; ("${COMMAND10[@]}"; touch COMMAND10_failed)&

        fi
		
		if [ -e COMMAND11_failed ]

        then

                # (Re)start Command11

                rm -f COMMAND11_failed; ("${COMMAND11[@]}"; touch COMMAND11_failed)&

        fi
		
		if [ -e COMMAND12_failed ]

        then

                # (Re)start Command12

                rm -f COMMAND12_failed; ("${COMMAND12[@]}"; touch COMMAND12_failed)&

        fi
		
		if [ -e COMMAND13_failed ]

        then

                # (Re)start Command13

                rm -f COMMAND13_failed; ("${COMMAND13[@]}"; touch COMMAND13_failed)&

        fi
		
		if [ -e COMMAND14_failed ]

        then

                # (Re)start Command14

                rm -f COMMAND14_failed; ("${COMMAND14[@]}"; touch COMMAND14_failed)&

        fi
		
		if [ -e COMMAND15_failed ]

        then

                # (Re)start Command15

                rm -f COMMAND15_failed; ("${COMMAND15[@]}"; touch COMMAND15_failed)&

        fi
		
		if [ -e COMMAND16_failed ]

        then

                # (Re)start Command16

                rm -f COMMAND16_failed; ("${COMMAND16[@]}"; touch COMMAND16_failed)&

        fi
		
		if [ -e COMMAND17_failed ]

        then

                # (Re)start Command17

                rm -f COMMAND17_failed; ("${COMMAND17[@]}"; touch COMMAND17_failed)&

        fi
		
		if [ -e COMMAND18_failed ]

        then

                # (Re)start Command18

                rm -f COMMAND18_failed; ("${COMMAND18[@]}"; touch COMMAND18_failed)&

        fi

        sleep 30

done
