# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_22:56:20_UTC-green)

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

**Latest saved flight:** 2026-06-16 22:56:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-16 22:56:20 UTC

- **112,516** saved flights
- **39,164** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **112,516** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,373,556.2 tonnes** estimated CO2 emissions
- **79,626,446 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4633 |
| 2 | SkyWest Airlines | 4201 |
| 3 | EJA | 2188 |
| 4 | IndiGo | 2187 |
| 5 | American Airlines | 1778 |
| 6 | Southwest Airlines | 1680 |
| 7 | ENY | 1408 |
| 8 | Delta Air Lines | 1333 |
| 9 | Lufthansa | 1263 |
| 10 | Vueling | 1029 |
| 11 | LATAM Airlines | 992 |
| 12 | WIF | 992 |
| 13 | AXM | 939 |
| 14 | AZU | 937 |
| 15 | LXJ | 859 |
| 16 | Swiss International | 804 |
| 17 | All Nippon Airways | 780 |
| 18 | Alaska Airlines | 760 |
| 19 | QLK | 736 |
| 20 | easyJet | 726 |
| 21 | EJU | 712 |
| 22 | Cathay Pacific | 664 |
| 23 | AEE | 632 |
| 24 | Air France | 626 |
| 25 | United Airlines | 626 |
| 26 | VIV | 626 |
| 27 | MXY | 598 |
| 28 | CXK | 593 |
| 29 | GLO | 555 |
| 30 | AXB | 552 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 94875 |
| 2 | 🇪🇸 ES | 7708 |
| 3 | 🇮🇳 IN | 6901 |
| 4 | 🇦🇺 AU | 6664 |
| 5 | 🇧🇷 BR | 6233 |
| 6 | 🇮🇹 IT | 6037 |
| 7 | 🇩🇪 DE | 6007 |
| 8 | 🇨🇦 CA | 5918 |
| 9 | 🇯🇵 JP | 5065 |
| 10 | 🇬🇧 GB | 4853 |
| 11 | 🇫🇷 FR | 4481 |
| 12 | 🇨🇴 CO | 3812 |
| 13 | 🇲🇽 MX | 3326 |
| 14 | 🇬🇷 GR | 3192 |
| 15 | 🇳🇴 NO | 3105 |
| 16 | 🇨🇭 CH | 2879 |
| 17 | 🇲🇾 MY | 2429 |
| 18 | 🇹🇷 TR | 2247 |
| 19 | 🇿🇦 ZA | 1911 |
| 20 | 🇰🇷 KR | 1853 |
| 21 | 🇳🇿 NZ | 1842 |
| 22 | 🇹🇭 TH | 1840 |
| 23 | 🇵🇱 PL | 1836 |
| 24 | 🇵🇭 PH | 1633 |
| 25 | 🇬🇹 GT | 1610 |
| 26 | 🇲🇦 MA | 1236 |
| 27 | 🇲🇴 MO | 1159 |
| 28 | 🇲🇪 ME | 1102 |
| 29 | 🇳🇱 NL | 1092 |
| 30 | 🇭🇷 HR | 977 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2404 |
| 2 | Denver International Airport |  | US | 1908 |
| 3 | Tokyo International Airport |  | JP | 1680 |
| 4 | Indira Gandhi International Airport |  | IN | 1502 |
| 5 | Guaymaral Airport |  | CO | 1413 |
| 6 | Harry Reid International Airport |  | US | 1413 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1387 |
| 8 | Zurich Airport |  | CH | 1264 |
| 9 | La Aurora Airport |  | GT | 1240 |
| 10 | Frankfurt am Main International Airport |  | DE | 1232 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1211 |
| 12 | Macau International Airport |  | MO | 1159 |
| 13 | El Dorado International Airport |  | CO | 1144 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1127 |
| 15 | Chicago O'Hare International Airport |  | US | 1122 |
| 16 | Capua Airport |  | IT | 976 |
| 17 | Madrid Barajas International Airport |  | ES | 975 |
| 18 | Salt Lake City International Airport |  | US | 952 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 945 |
| 20 | Kuala Lumpur International Airport |  | MY | 942 |
| 21 | Charlotte/Douglas International Airport |  | US | 870 |
| 22 | Congonhas Airport |  | BR | 866 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 841 |
| 24 | Charles de Gaulle International Airport |  | FR | 838 |
| 25 | Bengaluru International Airport |  | IN | 835 |
| 26 | Malpensa International Airport |  | IT | 814 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 778 |
| 28 | Ninoy Aquino International Airport |  | PH | 754 |
| 29 | Daniel K Inouye International Airport |  | US | 742 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 740 |
| 31 | Tenerife Norte Airport |  | ES | 738 |
| 32 | Barcelona International Airport |  | ES | 732 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 713 |
| 34 | Amsterdam Airport Schiphol |  | NL | 672 |
| 35 | Don Mueang International Airport |  | TH | 670 |
| 36 | Vitoria/Foronda Airport |  | ES | 667 |
| 37 | Calgary International Airport |  | CA | 665 |
| 38 | Seattle-Tacoma International Airport |  | US | 650 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 646 |
| 40 | Viracopos International Airport |  | BR | 641 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 586 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 409 | 21m | 244 km | 1,722.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 298 | 24m | 225 km | 1,156.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 293 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 272 | 1h 25m | 910 km | 4,268.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 265 | 1h 10m | 770 km | 3,520.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 225 | 26m | 275 km | 1,066.2 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 164 | 22m | 55 km | 155.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 163 | 27m | 215 km | 603.7 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 154 | 27m | 152 km | 402.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 152 | 31m | 369 km | 967.5 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 149 | 44m | 452 km | 1,161.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 143 | 44m | 241 km | 594.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 135 | 1h 1m | 695 km | 1,618.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 126 | 1h 17m | 961 km | 2,088.5 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 125 | 24m | 223 km | 480.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N408GG |  | KHTO (KHTO) | Linden Airport (KLDJ) | 2026-06-16 22:05 UTC | 2026-06-16 22:56 UTC | 51m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-06-16 22:11 UTC | 2026-06-16 22:54 UTC | 42m |
| N250RM |  | Pioneer Village Field (K0V3) | Lincoln Airport (KLNK) | 2026-06-16 22:26 UTC | 2026-06-16 22:48 UTC | 21m |
| N183TS |  | Nashville International Airport (KBNA) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-06-16 22:07 UTC | 2026-06-16 22:44 UTC | 36m |
| FXC66 | FXC | Bridgeport/Sikorsky Airport (KBDR) | Laguardia Airport (KLGA) | 2026-06-16 22:17 UTC | 2026-06-16 22:40 UTC | 22m |
| N377DJ |  | Ocean County Airport (KMJX) | Ocean County Airport (KMJX) | 2026-06-16 22:35 UTC | 2026-06-16 22:39 UTC | 4m |
| N29EF |  | Princeton Airport (K39N) | Lancaster Airport (KLNS) | 2026-06-16 21:59 UTC | 2026-06-16 22:36 UTC | 37m |
| LICHEN8 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-06-16 22:02 UTC | 2026-06-16 22:36 UTC | 33m |
| N52168 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-06-16 22:01 UTC | 2026-06-16 22:35 UTC | 33m |
| MISFIT2 | MIS | G Bar F Ranch Airport (NM84) | 81NM (81NM) | 2026-06-16 22:21 UTC | 2026-06-16 22:34 UTC | 12m |
| LPE2811 | LPE | Miami International Airport (KMIA) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-06-16 21:04 UTC | 2026-06-16 22:32 UTC | 1h 27m |
| CAP3041 | CAP | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | KWSD (KWSD) | 2026-06-16 21:51 UTC | 2026-06-16 22:30 UTC | 39m |
| JBU988 | JetBlue | Los Angeles International Airport (KLAX) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-16 17:17 UTC | 2026-06-16 22:30 UTC | 5h 12m |
| C6055 |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Camarillo Airport (KCMA) | 2026-06-16 22:21 UTC | 2026-06-16 22:29 UTC | 7m |
| SPR700 | SPR | Québec City Jean Lesage International Airport (CYQB) | Havelock Airport (CCS5) | 2026-06-16 21:35 UTC | 2026-06-16 22:29 UTC | 53m |
| N748MK |  | Lancaster Airport (KLNS) | Ocean City Municipal Airport (KOXB) | 2026-06-16 21:05 UTC | 2026-06-16 22:26 UTC | 1h 20m |
| UPS5768 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Dallas-Fort Worth International Airport (KDFW) | 2026-06-16 20:37 UTC | 2026-06-16 22:26 UTC | 1h 49m |
| ROGUE4 | ROG | Eric Marcus Municipal Airport (KP01) | Eric Marcus Municipal Airport (KP01) | 2026-06-16 21:54 UTC | 2026-06-16 22:20 UTC | 26m |
| EDG92 | EDG | Henderson Executive Airport (KHND) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-16 21:21 UTC | 2026-06-16 22:19 UTC | 58m |
| FFL1063 | FFL | Bend Municipal Airport (KBDN) | OG12 (OG12) | 2026-06-16 22:11 UTC | 2026-06-16 22:18 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
