# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_07:38:44_UTC-green)

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

**Latest saved flight:** 2026-08-10 07:38:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 07:38:44 UTC

- **183,439** saved flights
- **58,487** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **183,439** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,204,511.0 tonnes** estimated CO2 emissions
- **127,797,741 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7270 |
| 2 | SkyWest Airlines | 6684 |
| 3 | EJA | 3629 |
| 4 | IndiGo | 3206 |
| 5 | Southwest Airlines | 2882 |
| 6 | American Airlines | 2868 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2172 |
| 9 | LATAM Airlines | 1716 |
| 10 | AZU | 1646 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1516 |
| 13 | Vueling | 1509 |
| 14 | LXJ | 1451 |
| 15 | easyJet | 1255 |
| 16 | Swiss International | 1255 |
| 17 | AXM | 1230 |
| 18 | QLK | 1130 |
| 19 | EJU | 1124 |
| 20 | All Nippon Airways | 1118 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1012 |
| 23 | GLO | 984 |
| 24 | AEE | 956 |
| 25 | CXK | 953 |
| 26 | Air France | 949 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 931 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156984 |
| 2 | 🇪🇸 ES | 11764 |
| 3 | 🇧🇷 BR | 10535 |
| 4 | 🇦🇺 AU | 10274 |
| 5 | 🇮🇳 IN | 10035 |
| 6 | 🇨🇦 CA | 9993 |
| 7 | 🇮🇹 IT | 9481 |
| 8 | 🇩🇪 DE | 9070 |
| 9 | 🇬🇧 GB | 8493 |
| 10 | 🇯🇵 JP | 7462 |
| 11 | 🇫🇷 FR | 7290 |
| 12 | 🇨🇴 CO | 6864 |
| 13 | 🇬🇷 GR | 5376 |
| 14 | 🇲🇽 MX | 5248 |
| 15 | 🇨🇭 CH | 4888 |
| 16 | 🇹🇷 TR | 4768 |
| 17 | 🇳🇴 NO | 4708 |
| 18 | 🇲🇾 MY | 3205 |
| 19 | 🇵🇱 PL | 3068 |
| 20 | 🇿🇦 ZA | 3043 |
| 21 | 🇹🇭 TH | 2824 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2429 |
| 24 | 🇬🇹 GT | 2351 |
| 25 | 🇰🇷 KR | 2277 |
| 26 | 🇲🇦 MA | 1852 |
| 27 | 🇭🇷 HR | 1830 |
| 28 | 🇲🇪 ME | 1653 |
| 29 | 🇳🇱 NL | 1645 |
| 30 | 🇲🇴 MO | 1520 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3808 |
| 2 | Denver International Airport |  | US | 3036 |
| 3 | Tokyo International Airport |  | JP | 2311 |
| 4 | Indira Gandhi International Airport |  | IN | 2246 |
| 5 | Guaymaral Airport |  | CO | 2236 |
| 6 | Harry Reid International Airport |  | US | 2149 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1966 |
| 8 | Zurich Airport |  | CH | 1958 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1908 |
| 10 | La Aurora Airport |  | GT | 1804 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1645 |
| 13 | Salt Lake City International Airport |  | US | 1638 |
| 14 | Chicago O'Hare International Airport |  | US | 1637 |
| 15 | Frankfurt am Main International Airport |  | DE | 1585 |
| 16 | Congonhas Airport |  | BR | 1528 |
| 17 | Macau International Airport |  | MO | 1520 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1450 |
| 19 | Madrid Barajas International Airport |  | ES | 1439 |
| 20 | Capua Airport |  | IT | 1435 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1314 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1284 |
| 24 | Malpensa International Airport |  | IT | 1268 |
| 25 | Charles de Gaulle International Airport |  | FR | 1248 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1202 |
| 28 | Bengaluru International Airport |  | IN | 1190 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1148 |
| 30 | Ninoy Aquino International Airport |  | PH | 1145 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1082 |
| 33 | Seattle-Tacoma International Airport |  | US | 1057 |
| 34 | Viracopos International Airport |  | BR | 1054 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Daniel K Inouye International Airport |  | US | 1046 |
| 37 | Calgary International Airport |  | CA | 1046 |
| 38 | Oslo Gardermoen Airport |  | NO | 1014 |
| 39 | Tenerife Norte Airport |  | ES | 1000 |
| 40 | Amsterdam Airport Schiphol |  | NL | 992 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 674 | 21m | 244 km | 2,838.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 438 | 1h 8m | 770 km | 5,818.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 427 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 272 | 44m | 241 km | 1,129.8 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 258 | 1h 48m | 1,423 km | 6,331.7 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 255 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 247 | 20m | 250 km | 1,066.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 226 | 19m | 99 km | 387.1 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 219 | 19m | 144 km | 544.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 217 | 1h 38m | 1,156 km | 4,329.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 213 | 31m | 369 km | 1,355.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WWF287 | WWF | Roberts Field/Redmond Municipal Airport (KRDM) | Flying T Ranch Airport (5OR4) | 2026-08-10 07:07 UTC | 2026-08-10 07:38 UTC | 31m |
| ANA1278 | All Nippon Airways | New Chitose Airport (RJCC) | Ashiya Airport (RJFA) | 2026-08-10 05:50 UTC | 2026-08-10 07:36 UTC | 1h 45m |
| HKE638 | HKE | Chek Lap Kok International Airport (VHHH) | Iki Airport (RJDB) | 2026-08-10 04:41 UTC | 2026-08-10 07:35 UTC | 2h 54m |
| SKY019 | SKY | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-10 06:19 UTC | 2026-08-10 07:32 UTC | 1h 12m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-10 07:16 UTC | 2026-08-10 07:27 UTC | 11m |
|  |  | Haifa International Airport (LLHA) | Haifa International Airport (LLHA) | 2026-08-10 07:06 UTC | 2026-08-10 07:26 UTC | 20m |
| NV131 |  | Mount Gambier Airport (YMTG) | Melbourne Essendon Airport (YMEN) | 2026-08-10 06:37 UTC | 2026-08-10 07:16 UTC | 38m |
| ALFT5 | ALF | Bellingham International Airport (KBLI) | Boeing Field/King County International Airport (KBFI) | 2026-08-10 06:37 UTC | 2026-08-10 07:15 UTC | 38m |
| ECOLT | ECO | Jerez Airport (LEJR) | LEVE (LEVE) | 2026-08-10 06:16 UTC | 2026-08-10 07:15 UTC | 58m |
| OYA210 | OYA | Zwara Airport (HLZW) | Zwara Airport (HLZW) | 2026-08-10 07:08 UTC | 2026-08-10 07:10 UTC | 2m |
| VSB92 | VSB | Barrow Walney Island Airport (EGNL) | Bristol International Airport (EGGD) | 2026-08-10 06:35 UTC | 2026-08-10 07:10 UTC | 34m |
| NIA526 | NIA | Sharm El Sheikh International Airport (HESH) | Hulwan (HE15) | 2026-08-10 06:38 UTC | 2026-08-10 07:06 UTC | 28m |
| KLM1229 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Gothenburg-Landvetter Airport (ESGG) | 2026-08-10 06:03 UTC | 2026-08-10 07:05 UTC | 1h 2m |
| AFR17NX | Air France | Charles de Gaulle International Airport (LFPG) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-10 05:36 UTC | 2026-08-10 07:02 UTC | 1h 26m |
| SAS024 | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Ornskoldsvik Airport (ESNO) | 2026-08-10 06:19 UTC | 2026-08-10 06:55 UTC | 35m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-08-10 05:35 UTC | 2026-08-10 06:54 UTC | 1h 18m |
| WIF1X | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-10 06:41 UTC | 2026-08-10 06:51 UTC | 10m |
| ZKIWG | ZKI | Mandeville Aerodrome (NZVL) | Invercargill Airport (NZNV) | 2026-08-10 06:12 UTC | 2026-08-10 06:50 UTC | 38m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-10 06:13 UTC | 2026-08-10 06:49 UTC | 35m |
| ASL32B | ASL | Belgrade Nikola Tesla Airport (LYBE) | Gothenburg-Landvetter Airport (ESGG) | 2026-08-10 04:43 UTC | 2026-08-10 06:47 UTC | 2h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
