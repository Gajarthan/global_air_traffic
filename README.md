# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_09:25:08_UTC-green)

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

**Latest saved flight:** 2026-07-23 09:25:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 09:25:08 UTC

- **145,238** saved flights
- **48,612** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **145,238** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,740,732.8 tonnes** estimated CO2 emissions
- **100,912,044 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5891 |
| 2 | SkyWest Airlines | 5317 |
| 3 | EJA | 2862 |
| 4 | IndiGo | 2632 |
| 5 | American Airlines | 2322 |
| 6 | Southwest Airlines | 2194 |
| 7 | ENY | 1808 |
| 8 | Delta Air Lines | 1720 |
| 9 | Lufthansa | 1445 |
| 10 | LATAM Airlines | 1338 |
| 11 | AZU | 1250 |
| 12 | Vueling | 1238 |
| 13 | WIF | 1237 |
| 14 | LXJ | 1117 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1029 |
| 17 | easyJet | 943 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 915 |
| 20 | QLK | 913 |
| 21 | EJU | 888 |
| 22 | VIV | 809 |
| 23 | CXK | 779 |
| 24 | AEE | 768 |
| 25 | JetBlue | 766 |
| 26 | Air France | 765 |
| 27 | MXY | 760 |
| 28 | Cathay Pacific | 757 |
| 29 | United Airlines | 755 |
| 30 | GLO | 745 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 125156 |
| 2 | 🇪🇸 ES | 9408 |
| 3 | 🇦🇺 AU | 8336 |
| 4 | 🇮🇳 IN | 8243 |
| 5 | 🇧🇷 BR | 8195 |
| 6 | 🇨🇦 CA | 7717 |
| 7 | 🇮🇹 IT | 7552 |
| 8 | 🇩🇪 DE | 7479 |
| 9 | 🇬🇧 GB | 6622 |
| 10 | 🇯🇵 JP | 6085 |
| 11 | 🇫🇷 FR | 5769 |
| 12 | 🇨🇴 CO | 4745 |
| 13 | 🇲🇽 MX | 4231 |
| 14 | 🇬🇷 GR | 4114 |
| 15 | 🇳🇴 NO | 3874 |
| 16 | 🇨🇭 CH | 3756 |
| 17 | 🇹🇷 TR | 3402 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2445 |
| 20 | 🇿🇦 ZA | 2352 |
| 21 | 🇳🇿 NZ | 2223 |
| 22 | 🇹🇭 TH | 2138 |
| 23 | 🇰🇷 KR | 2045 |
| 24 | 🇵🇭 PH | 1939 |
| 25 | 🇬🇹 GT | 1887 |
| 26 | 🇲🇦 MA | 1504 |
| 27 | 🇲🇪 ME | 1444 |
| 28 | 🇳🇱 NL | 1357 |
| 29 | 🇭🇷 HR | 1321 |
| 30 | 🇲🇴 MO | 1213 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2999 |
| 2 | Denver International Airport |  | US | 2431 |
| 3 | Tokyo International Airport |  | JP | 1956 |
| 4 | Indira Gandhi International Airport |  | IN | 1829 |
| 5 | Harry Reid International Airport |  | US | 1822 |
| 6 | Guaymaral Airport |  | CO | 1777 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1648 |
| 8 | Zurich Airport |  | CH | 1603 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1524 |
| 10 | La Aurora Airport |  | GT | 1462 |
| 11 | Frankfurt am Main International Airport |  | DE | 1392 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1371 |
| 13 | Chicago O'Hare International Airport |  | US | 1350 |
| 14 | Salt Lake City International Airport |  | US | 1305 |
| 15 | El Dorado International Airport |  | CO | 1298 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1262 |
| 17 | Macau International Airport |  | MO | 1213 |
| 18 | Capua Airport |  | IT | 1179 |
| 19 | Congonhas Airport |  | BR | 1166 |
| 20 | Madrid Barajas International Airport |  | ES | 1157 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1145 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1041 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1015 |
| 26 | Charles de Gaulle International Airport |  | FR | 1010 |
| 27 | Bengaluru International Airport |  | IN | 985 |
| 28 | Malpensa International Airport |  | IT | 938 |
| 29 | Ninoy Aquino International Airport |  | PH | 905 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 890 |
| 31 | Barcelona International Airport |  | ES | 881 |
| 32 | Daniel K Inouye International Airport |  | US | 879 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 866 |
| 34 | Tenerife Norte Airport |  | ES | 831 |
| 35 | Seattle-Tacoma International Airport |  | US | 827 |
| 36 | Viracopos International Airport |  | BR | 825 |
| 37 | Calgary International Airport |  | CA | 825 |
| 38 | Scottsdale Airport |  | US | 823 |
| 39 | Amsterdam Airport Schiphol |  | NL | 817 |
| 40 | Oslo Gardermoen Airport |  | NO | 798 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 749 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 528 | 21m | 244 km | 2,223.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 351 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 343 | 1h 9m | 770 km | 4,556.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 261 | 26m | 275 km | 1,236.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 258 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 217 | 22m | 55 km | 206.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 193 | 44m | 241 km | 801.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 192 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 165 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EFW35LD | EFW | London Gatwick Airport (EGKK) | Decimomannu Airport (LIED) | 2026-07-23 07:35 UTC | 2026-07-23 09:25 UTC | 1h 49m |
| SPSDW | SPS | Zamość-Mokre Airport (EPZA) | Zamość-Mokre Airport (EPZA) | 2026-07-23 09:02 UTC | 2026-07-23 09:16 UTC | 14m |
| 5YPCX |  | Nairobi Wilson Airport (HKNW) | Nairobi Wilson Airport (HKNW) | 2026-07-23 09:12 UTC | 2026-07-23 09:15 UTC | 2m |
| EXS1623 | EXS | London Stansted Airport (EGSS) | Samos Airport (LGSM) | 2026-07-23 06:10 UTC | 2026-07-23 09:14 UTC | 3h 4m |
| RVP951 | RVP | Cascais Airport (LPCS) | Portimão Airport (LPPM) | 2026-07-23 08:28 UTC | 2026-07-23 09:08 UTC | 40m |
| CWA935 | CWA | Edmonton International Airport (CYEG) | Glendon Airport (CFP5) | 2026-07-23 08:43 UTC | 2026-07-23 09:08 UTC | 24m |
| BTN701 | BTN | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-07-23 06:36 UTC | 2026-07-23 08:54 UTC | 2h 18m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-07-22 21:59 UTC | 2026-07-23 08:52 UTC | 10h 53m |
| YOP | YOP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-23 08:22 UTC | 2026-07-23 08:49 UTC | 27m |
| NAK706B | NAK | Montlucon-Gueret Airport (LFBK) | Clermont-Ferrand Auvergne Airport (LFLC) | 2026-07-23 08:15 UTC | 2026-07-23 08:48 UTC | 33m |
| MDA791 | MDA | Taichung Ching Chuang Kang Airport (RCMQ) | Makung Airport (RCQC) | 2026-07-23 08:23 UTC | 2026-07-23 08:45 UTC | 22m |
| DLH8PF | Lufthansa | Munich International Airport (EDDM) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-23 07:38 UTC | 2026-07-23 08:45 UTC | 1h 6m |
| FGTHA | FGT | Gap - Tallard Airport (LFNA) | Gap - Tallard Airport (LFNA) | 2026-07-23 07:55 UTC | 2026-07-23 08:34 UTC | 38m |
| ANA319 | All Nippon Airways | Tokyo International Airport (RJTT) | Toyama Airport (RJNT) | 2026-07-23 08:02 UTC | 2026-07-23 08:31 UTC | 29m |
| AHX106 | AHX | Fukuoka Airport (RJFF) | Kumamoto Airport (RJFT) | 2026-07-23 08:16 UTC | 2026-07-23 08:31 UTC | 15m |
|  |  | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-23 08:16 UTC | 2026-07-23 08:30 UTC | 14m |
| FD613 |  | Perth Jandakot Airport (YPJT) | Dongara Airport (YDRA) | 2026-07-23 07:49 UTC | 2026-07-23 08:30 UTC | 41m |
| ANA297 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-07-23 07:48 UTC | 2026-07-23 08:30 UTC | 41m |
| ICEPV | ICE | Perugia / San Egidio Airport (LIRZ) | L'Aquila / Preturo Airport (LIAP) | 2026-07-23 07:57 UTC | 2026-07-23 08:28 UTC | 31m |
| AWQ176 | AWQ | Soekarno-Hatta International Airport (WIII) | WIAT (WIAT) | 2026-07-23 08:11 UTC | 2026-07-23 08:28 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
