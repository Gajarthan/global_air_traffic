# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_16:13:27_UTC-green)

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

**Latest saved flight:** 2026-08-09 16:13:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 16:13:27 UTC

- **181,554** saved flights
- **57,988** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **181,554** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,181,999.5 tonnes** estimated CO2 emissions
- **126,492,723 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7203 |
| 2 | SkyWest Airlines | 6589 |
| 3 | EJA | 3563 |
| 4 | IndiGo | 3190 |
| 5 | Southwest Airlines | 2846 |
| 6 | American Airlines | 2822 |
| 7 | ENY | 2255 |
| 8 | Delta Air Lines | 2146 |
| 9 | LATAM Airlines | 1697 |
| 10 | AZU | 1626 |
| 11 | Lufthansa | 1614 |
| 12 | Vueling | 1504 |
| 13 | WIF | 1503 |
| 14 | LXJ | 1410 |
| 15 | Swiss International | 1244 |
| 16 | easyJet | 1243 |
| 17 | AXM | 1226 |
| 18 | QLK | 1116 |
| 19 | EJU | 1111 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 998 |
| 23 | GLO | 971 |
| 24 | CXK | 949 |
| 25 | AEE | 948 |
| 26 | Cathay Pacific | 947 |
| 27 | Air France | 939 |
| 28 | United Airlines | 931 |
| 29 | PGT | 915 |
| 30 | MXY | 909 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 155137 |
| 2 | 🇪🇸 ES | 11702 |
| 3 | 🇧🇷 BR | 10426 |
| 4 | 🇦🇺 AU | 10202 |
| 5 | 🇮🇳 IN | 9994 |
| 6 | 🇨🇦 CA | 9878 |
| 7 | 🇮🇹 IT | 9407 |
| 8 | 🇩🇪 DE | 9007 |
| 9 | 🇬🇧 GB | 8404 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7236 |
| 12 | 🇨🇴 CO | 6742 |
| 13 | 🇬🇷 GR | 5324 |
| 14 | 🇲🇽 MX | 5180 |
| 15 | 🇨🇭 CH | 4854 |
| 16 | 🇹🇷 TR | 4698 |
| 17 | 🇳🇴 NO | 4677 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3052 |
| 20 | 🇿🇦 ZA | 3011 |
| 21 | 🇹🇭 TH | 2802 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2305 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1837 |
| 27 | 🇭🇷 HR | 1811 |
| 28 | 🇲🇪 ME | 1645 |
| 29 | 🇳🇱 NL | 1635 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3744 |
| 2 | Denver International Airport |  | US | 2989 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2230 |
| 5 | Guaymaral Airport |  | CO | 2228 |
| 6 | Harry Reid International Airport |  | US | 2128 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1954 |
| 8 | Zurich Airport |  | CH | 1939 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1881 |
| 10 | La Aurora Airport |  | GT | 1770 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1649 |
| 12 | Chicago O'Hare International Airport |  | US | 1629 |
| 13 | El Dorado International Airport |  | CO | 1619 |
| 14 | Salt Lake City International Airport |  | US | 1618 |
| 15 | Frankfurt am Main International Airport |  | DE | 1579 |
| 16 | Macau International Airport |  | MO | 1518 |
| 17 | Congonhas Airport |  | BR | 1512 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1440 |
| 19 | Madrid Barajas International Airport |  | ES | 1431 |
| 20 | Capua Airport |  | IT | 1419 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1354 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1297 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1253 |
| 25 | Charles de Gaulle International Airport |  | FR | 1234 |
| 26 | Charlotte/Douglas International Airport |  | US | 1226 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Ninoy Aquino International Airport |  | PH | 1135 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1127 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1110 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1045 |
| 34 | Daniel K Inouye International Airport |  | US | 1042 |
| 35 | Seattle-Tacoma International Airport |  | US | 1042 |
| 36 | Reno/Tahoe International Airport |  | US | 1034 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1007 |
| 39 | Tenerife Norte Airport |  | ES | 993 |
| 40 | Vitoria/Foronda Airport |  | ES | 986 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 920 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 419 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 255 | 1h 48m | 1,423 km | 6,258.1 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 245 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 242 | 20m | 250 km | 1,045.3 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 228 | 26m | 215 km | 844.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 223 | 19m | 99 km | 382.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 219 | 1h 15m | 961 km | 3,630.0 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 217 | 19m | 144 km | 539.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 214 | 1h 38m | 1,156 km | 4,269.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 212 | 24m | 218 km | 798.7 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFR608 | CFR | Chino Airport (KCNO) | Corona Municipal Airport (KAJO) | 2026-08-09 15:52 UTC | 2026-08-09 16:13 UTC | 20m |
| ABF8 | ABF | Cannes-Mandelieu Airport (LFMD) | Stockholm-Bromma Airport (ESSB) | 2026-08-09 13:41 UTC | 2026-08-09 16:11 UTC | 2h 29m |
| ES801 |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Mather Airport (KMHR) | 2026-08-09 15:29 UTC | 2026-08-09 16:03 UTC | 33m |
| N115GK |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-08-09 15:24 UTC | 2026-08-09 15:55 UTC | 30m |
| DAL2105 | Delta Air Lines | Noahs Ark Airport (06MO) | Seattle-Tacoma International Airport (KSEA) | 2026-08-09 12:28 UTC | 2026-08-09 15:52 UTC | 3h 23m |
| ROPER94 | ROP | Boise Air Trml/Gowen Field (KBOI) | Buckley Space Force Base Airport (KBKF) | 2026-08-09 13:54 UTC | 2026-08-09 15:47 UTC | 1h 53m |
| N682AC |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-08-09 15:08 UTC | 2026-08-09 15:46 UTC | 37m |
| XBMCB | XBM | Del Norte International Airport (MMAN) | Mina Hercules Airport (MM68) | 2026-08-09 15:23 UTC | 2026-08-09 15:46 UTC | 22m |
| PFT420 | PFT | NV13 (NV13) | Buchanan Field (KCCR) | 2026-08-09 15:17 UTC | 2026-08-09 15:44 UTC | 27m |
| IGO083 | IndiGo | Indira Gandhi International Airport (VIDP) | Ras Tanura Airport (OERT) | 2026-08-09 11:58 UTC | 2026-08-09 15:44 UTC | 3h 46m |
| GPJCD | GPJ | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-08-09 15:19 UTC | 2026-08-09 15:41 UTC | 21m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-09 15:25 UTC | 2026-08-09 15:39 UTC | 14m |
| AAL1978 | American Airlines | Ronald Reagan Washington Ntl Airport (KDCA) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-09 13:01 UTC | 2026-08-09 15:39 UTC | 2h 37m |
| N9304F |  | Harford County Airport (K0W3) | Harford County Airport (K0W3) | 2026-08-09 15:26 UTC | 2026-08-09 15:36 UTC | 9m |
| CHX1 | CHX | Oberschleisheim Airfield (EDNX) | Innsbruck Airport (LOWI) | 2026-08-09 15:14 UTC | 2026-08-09 15:34 UTC | 20m |
| N241MP |  | AL02 (AL02) | AL02 (AL02) | 2026-08-09 15:17 UTC | 2026-08-09 15:34 UTC | 17m |
| N283HG |  | Denton Enterprise Airport (KDTO) | Decatur Municipal Airport (KLUD) | 2026-08-09 15:17 UTC | 2026-08-09 15:32 UTC | 15m |
| AELIA95 | AEL | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Raron Airport (LSTA) | 2026-08-09 14:47 UTC | 2026-08-09 15:31 UTC | 43m |
| CFGMF | CFG | Brampton Airport (CNC3) | Brampton Airport (CNC3) | 2026-08-09 14:59 UTC | 2026-08-09 15:30 UTC | 30m |
| N448ME |  | Weiblen Airport (TE13) | Kelly Field (KSKF) | 2026-08-09 15:21 UTC | 2026-08-09 15:28 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
