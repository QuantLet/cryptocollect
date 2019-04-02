#!/bin/bash
cd ~/cryptocollect/logs

COMMAND0=(python ~/cryptocollect/scripts/cbpro.py)
COMMAND1=(python ~/cryptocollect/scripts/bitfinex_bch.py)
COMMAND2=(python ~/cryptocollect/scripts/bitfinex_btc.py)
COMMAND3=(python ~/cryptocollect/scripts/bitfinex_dash.py)
COMMAND4=(python ~/cryptocollect/scripts/bitfinex_eos.py)
COMMAND5=(python ~/cryptocollect/scripts/bitfinex_etc.py)
COMMAND6=(python ~/cryptocollect/scripts/bitfinex_eth.py)
COMMAND7=(python ~/cryptocollect/scripts/bitfinex_iota.py)
COMMAND8=(python ~/cryptocollect/scripts/bitfinex_ltc.py)
COMMAND9=(python ~/cryptocollect/scripts/bitfinex_xlm.py)
COMMAND10=(python ~/cryptocollect/scripts/bitfinex_xmr.py)
COMMAND11=(python ~/cryptocollect/scripts/bitfinex_xrp.py)
COMMAND12=(python ~/cryptocollect/scripts/bitfinex_zrx.py)
COMMAND13=(python ~/cryptocollect/scripts/binance.py)
COMMAND14=(python ~/cryptocollect/scripts/okex_bch.py)
COMMAND15=(python ~/cryptocollect/scripts/okex_btc.py)
COMMAND16=(python ~/cryptocollect/scripts/okex_etc.py)
COMMAND17=(python ~/cryptocollect/scripts/okex_eth.py)
COMMAND18=(python ~/cryptocollect/scripts/okex_ltc.py)
COMMAND19=(python ~/cryptocollect/scripts/hitbtc_bch.py)
COMMAND20=(python ~/cryptocollect/scripts/hitbtc_btc.py)
COMMAND21=(python ~/cryptocollect/scripts/hitbtc_dash.py)
COMMAND22=(python ~/cryptocollect/scripts/hitbtc_eos.py)
COMMAND23=(python ~/cryptocollect/scripts/hitbtc_etc.py)
COMMAND24=(python ~/cryptocollect/scripts/hitbtc_eth.py)
COMMAND25=(python ~/cryptocollect/scripts/hitbtc_iota.py)
COMMAND26=(python ~/cryptocollect/scripts/hitbtc_ltc.py)
COMMAND27=(python ~/cryptocollect/scripts/hitbtc_xlm.py)
COMMAND28=(python ~/cryptocollect/scripts/hitbtc_xmr.py)
COMMAND29=(python ~/cryptocollect/scripts/hitbtc_xrp.py)
COMMAND30=(python ~/cryptocollect/scripts/hitbtc_zrx.py)
COMMAND31=(python ~/cryptocollect/scripts/bitstamp_bch.py)
COMMAND32=(python ~/cryptocollect/scripts/bitstamp_btc.py)
COMMAND33=(python ~/cryptocollect/scripts/bitstamp_eth.py)
COMMAND34=(python ~/cryptocollect/scripts/bitstamp_ltc.py)
COMMAND35=(python ~/cryptocollect/scripts/bitstamp_xrp.py)

touch COMMAND0_failed
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
touch COMMAND19_failed
touch COMMAND20_failed
touch COMMAND21_failed
touch COMMAND22_failed
touch COMMAND23_failed
touch COMMAND24_failed
touch COMMAND25_failed
touch COMMAND26_failed
touch COMMAND27_failed
touch COMMAND28_failed
touch COMMAND29_failed
touch COMMAND30_failed
touch COMMAND31_failed
touch COMMAND32_failed
touch COMMAND33_failed
touch COMMAND34_failed
touch COMMAND35_failed

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

		if [ -e COMMAND19_failed ]

        then

                # (Re)start Command19

                rm -f COMMAND19_failed; ("${COMMAND19[@]}"; touch COMMAND19_failed)&

        fi

		if [ -e COMMAND20_failed ]

        then

                # (Re)start Command20

                rm -f COMMAND20_failed; ("${COMMAND20[@]}"; touch COMMAND20_failed)&

        fi

		if [ -e COMMAND21_failed ]

        then

                # (Re)start Command21

                rm -f COMMAND21_failed; ("${COMMAND21[@]}"; touch COMMAND21_failed)&

        fi

		if [ -e COMMAND22_failed ]

        then

                # (Re)start Command22

                rm -f COMMAND22_failed; ("${COMMAND22[@]}"; touch COMMAND22_failed)&

        fi




		if [ -e COMMAND23_failed ]

        then

                # (Re)start Command23

                rm -f COMMAND23_failed; ("${COMMAND23[@]}"; touch COMMAND23_failed)&

        fi




		if [ -e COMMAND24_failed ]

        then

                # (Re)start Command24

                rm -f COMMAND24_failed; ("${COMMAND24[@]}"; touch COMMAND24_failed)&

        fi




		if [ -e COMMAND25_failed ]

        then

                # (Re)start Command25

                rm -f COMMAND25_failed; ("${COMMAND25[@]}"; touch COMMAND25_failed)&

        fi




		if [ -e COMMAND26_failed ]

        then

                # (Re)start Command26

                rm -f COMMAND26_failed; ("${COMMAND26[@]}"; touch COMMAND26_failed)&

        fi




		if [ -e COMMAND27_failed ]

        then

                # (Re)start Command27

                rm -f COMMAND27_failed; ("${COMMAND27[@]}"; touch COMMAND27_failed)&

        fi




		if [ -e COMMAND28_failed ]

        then

                # (Re)start Command28

                rm -f COMMAND28_failed; ("${COMMAND28[@]}"; touch COMMAND28_failed)&

        fi




		if [ -e COMMAND29_failed ]

        then

                # (Re)start Command29

                rm -f COMMAND29_failed; ("${COMMAND29[@]}"; touch COMMAND29_failed)&

        fi




		if [ -e COMMAND30_failed ]

        then

                # (Re)start Command30

                rm -f COMMAND30_failed; ("${COMMAND30[@]}"; touch COMMAND30_failed)&

        fi




		if [ -e COMMAND31_failed ]

        then

                # (Re)start Command31

                rm -f COMMAND31_failed; ("${COMMAND31[@]}"; touch COMMAND31_failed)&

        fi




		if [ -e COMMAND32_failed ]

        then

                # (Re)start Command32

                rm -f COMMAND32_failed; ("${COMMAND32[@]}"; touch COMMAND32_failed)&

        fi




		if [ -e COMMAND33_failed ]

        then

                # (Re)start Command33

                rm -f COMMAND33_failed; ("${COMMAND33[@]}"; touch COMMAND33_failed)&

        fi




		if [ -e COMMAND34_failed ]

        then

                # (Re)start Command34

                rm -f COMMAND34_failed; ("${COMMAND34[@]}"; touch COMMAND34_failed)&

        fi




		if [ -e COMMAND35_failed ]

        then

                # (Re)start Command35

                rm -f COMMAND35_failed; ("${COMMAND35[@]}"; touch COMMAND35_failed)&

        fi






        sleep 60

done
