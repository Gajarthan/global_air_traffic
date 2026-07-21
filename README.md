# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_00:43:55_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-07-21 00:43:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-21 00:43:55 UTC

- **143,020** saved flights
- **47,949** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **143,020** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,715,078.4 tonnes** estimated CO2 emissions
- **99,424,833 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5815 |
| 2 | SkyWest Airlines | 5236 |
| 3 | EJA | 2819 |
| 4 | IndiGo | 2599 |
| 5 | American Airlines | 2293 |
| 6 | Southwest Airlines | 2158 |
| 7 | ENY | 1777 |
| 8 | Delta Air Lines | 1696 |
| 9 | Lufthansa | 1435 |
| 10 | LATAM Airlines | 1319 |
| 11 | AZU | 1230 |
| 12 | Vueling | 1227 |
| 13 | WIF | 1220 |
| 14 | LXJ | 1099 |
| 15 | AXM | 1057 |
| 16 | Swiss International | 1015 |
| 17 | easyJet | 933 |
| 18 | All Nippon Airways | 917 |
| 19 | Alaska Airlines | 903 |
| 20 | QLK | 901 |
| 21 | EJU | 879 |
| 22 | VIV | 796 |
| 23 | CXK | 765 |
| 24 | AEE | 763 |
| 25 | JetBlue | 760 |
| 26 | Air France | 759 |
| 27 | MXY | 744 |
| 28 | United Airlines | 743 |
| 29 | Cathay Pacific | 737 |
| 30 | GLO | 731 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 123136 |
| 2 | 🇪🇸 ES | 9309 |
| 3 | 🇦🇺 AU | 8201 |
| 4 | 🇮🇳 IN | 8142 |
| 5 | 🇧🇷 BR | 8071 |
| 6 | 🇨🇦 CA | 7538 |
| 7 | 🇮🇹 IT | 7442 |
| 8 | 🇩🇪 DE | 7393 |
| 9 | 🇬🇧 GB | 6544 |
| 10 | 🇯🇵 JP | 5997 |
| 11 | 🇫🇷 FR | 5672 |
| 12 | 🇨🇴 CO | 4590 |
| 13 | 🇲🇽 MX | 4158 |
| 14 | 🇬🇷 GR | 4068 |
| 15 | 🇳🇴 NO | 3820 |
| 16 | 🇨🇭 CH | 3692 |
| 17 | 🇹🇷 TR | 3378 |
| 18 | 🇲🇾 MY | 2758 |
| 19 | 🇵🇱 PL | 2403 |
| 20 | 🇿🇦 ZA | 2326 |
| 21 | 🇳🇿 NZ | 2203 |
| 22 | 🇹🇭 TH | 2128 |
| 23 | 🇰🇷 KR | 2032 |
| 24 | 🇵🇭 PH | 1928 |
| 25 | 🇬🇹 GT | 1874 |
| 26 | 🇲🇦 MA | 1492 |
| 27 | 🇲🇪 ME | 1416 |
| 28 | 🇳🇱 NL | 1345 |
| 29 | 🇭🇷 HR | 1301 |
| 30 | 🇲🇴 MO | 1194 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2950 |
| 2 | Denver International Airport |  | US | 2400 |
| 3 | Tokyo International Airport |  | JP | 1934 |
| 4 | Indira Gandhi International Airport |  | IN | 1805 |
| 5 | Harry Reid International Airport |  | US | 1798 |
| 6 | Guaymaral Airport |  | CO | 1738 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1637 |
| 8 | Zurich Airport |  | CH | 1585 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1502 |
| 10 | La Aurora Airport |  | GT | 1450 |
| 11 | Frankfurt am Main International Airport |  | DE | 1385 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1354 |
| 13 | Chicago O'Hare International Airport |  | US | 1336 |
| 14 | Salt Lake City International Airport |  | US | 1282 |
| 15 | El Dorado International Airport |  | CO | 1267 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1257 |
| 17 | Macau International Airport |  | MO | 1194 |
| 18 | Capua Airport |  | IT | 1166 |
| 19 | Congonhas Airport |  | BR | 1147 |
| 20 | Madrid Barajas International Airport |  | ES | 1147 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1132 |
| 22 | Kuala Lumpur International Airport |  | MY | 1065 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1039 |
| 24 | Charlotte/Douglas International Airport |  | US | 1033 |
| 25 | Charles de Gaulle International Airport |  | FR | 1004 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1000 |
| 27 | Bengaluru International Airport |  | IN | 972 |
| 28 | Malpensa International Airport |  | IT | 921 |
| 29 | Ninoy Aquino International Airport |  | PH | 900 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 877 |
| 31 | Daniel K Inouye International Airport |  | US | 871 |
| 32 | Barcelona International Airport |  | ES | 869 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 850 |
| 34 | Tenerife Norte Airport |  | ES | 825 |
| 35 | Calgary International Airport |  | CA | 816 |
| 36 | Seattle-Tacoma International Airport |  | US | 814 |
| 37 | Viracopos International Airport |  | BR | 811 |
| 38 | Amsterdam Airport Schiphol |  | NL | 808 |
| 39 | Scottsdale Airport |  | US | 806 |
| 40 | Vitoria/Foronda Airport |  | ES | 786 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 732 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 521 | 21m | 244 km | 2,193.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 349 | 24m | 225 km | 1,354.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 346 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 339 | 1h 9m | 770 km | 4,503.4 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 212 | 22m | 55 km | 201.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 192 | 1h 46m | 1,423 km | 4,712.0 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 166 | 1h 16m | 961 km | 2,751.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 163 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 158 | 14m | 154 km | 418.6 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AER180 | AER | King Salmon Airport (PAKN) | Homer Airport (PAHO) | 2026-07-20 23:59 UTC | 2026-07-21 00:43 UTC | 44m |
| N173BH |  | Pueblo Memorial Airport (KPUB) | Ak Su Airport (CO61) | 2026-07-21 00:19 UTC | 2026-07-21 00:43 UTC | 24m |
| JST565 | JST | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-07-20 22:35 UTC | 2026-07-21 00:41 UTC | 2h 6m |
| N86ME |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-07-21 00:25 UTC | 2026-07-21 00:41 UTC | 15m |
| JJA1325 | JJA | Gimpo International Airport (RKSS) | Kansai International Airport (RJBB) | 2026-07-20 23:18 UTC | 2026-07-21 00:40 UTC | 1h 21m |
| N7481T |  | Angwin-Parrett Field (K2O3) | Willows/Glenn County Airport (KWLW) | 2026-07-21 00:05 UTC | 2026-07-21 00:37 UTC | 31m |
| N8118Q |  | Long Island Mac Arthur Airport (KISP) | Tweed/New Haven Airport (KHVN) | 2026-07-21 00:16 UTC | 2026-07-21 00:35 UTC | 19m |
| TEXGLD | TEX | RNZAF Base Ohakea (NZOH) | Wanganui Airport (NZWU) | 2026-07-20 23:33 UTC | 2026-07-21 00:33 UTC | 1h 0m |
| BULET47 | BUL | San Clemente Island Nalf Airport (KNUC) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-20 22:12 UTC | 2026-07-21 00:32 UTC | 2h 20m |
| LN274AH |  | Charlotte/Douglas International Airport (KCLT) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-20 23:30 UTC | 2026-07-21 00:30 UTC | 1h 0m |
| YOQ | YOQ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-20 23:54 UTC | 2026-07-21 00:29 UTC | 35m |
| N809SA |  | Northway Airport (PAOR) | Tok Junction Airport (PFTO) | 2026-07-20 22:54 UTC | 2026-07-21 00:28 UTC | 1h 33m |
| N82BH |  | Fremont County Airport (K1V6) | Ak Su Airport (CO61) | 2026-07-21 00:05 UTC | 2026-07-21 00:26 UTC | 21m |
| AAL2504 | American Airlines | Savannah/Hilton Head International Airport (KSAV) | Philadelphia International Airport (KPHL) | 2026-07-20 22:44 UTC | 2026-07-21 00:24 UTC | 1h 40m |
| LXJ438 | LXJ | Van Nuys Airport (KVNY) | Vancouver International Airport (CYVR) | 2026-07-20 22:09 UTC | 2026-07-21 00:20 UTC | 2h 10m |
| N857WA |  | Hayward Executive Airport (KHWD) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-20 23:51 UTC | 2026-07-21 00:19 UTC | 28m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-20 23:43 UTC | 2026-07-21 00:18 UTC | 35m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-07-20 23:41 UTC | 2026-07-21 00:17 UTC | 36m |
| CFR76 | CFR | Porterville Municipal Airport (KPTV) | Sequoia Ranch Airport (CA44) | 2026-07-21 00:08 UTC | 2026-07-21 00:17 UTC | 9m |
| BOE352 | BOE | Renton Municipal Airport (KRNT) | Warden Airport (K2S4) | 2026-07-20 22:38 UTC | 2026-07-21 00:13 UTC | 1h 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
