# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_18:03:44_UTC-green)

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

**Latest saved flight:** 2026-07-23 18:03:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 18:03:44 UTC

- **146,086** saved flights
- **48,862** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **146,086** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,748,923.8 tonnes** estimated CO2 emissions
- **101,386,886 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5923 |
| 2 | SkyWest Airlines | 5338 |
| 3 | EJA | 2877 |
| 4 | IndiGo | 2645 |
| 5 | American Airlines | 2328 |
| 6 | Southwest Airlines | 2207 |
| 7 | ENY | 1816 |
| 8 | Delta Air Lines | 1729 |
| 9 | Lufthansa | 1449 |
| 10 | LATAM Airlines | 1346 |
| 11 | AZU | 1257 |
| 12 | Vueling | 1241 |
| 13 | WIF | 1240 |
| 14 | LXJ | 1124 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1034 |
| 17 | easyJet | 943 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 916 |
| 20 | QLK | 913 |
| 21 | EJU | 896 |
| 22 | VIV | 812 |
| 23 | CXK | 785 |
| 24 | AEE | 775 |
| 25 | JetBlue | 770 |
| 26 | Air France | 768 |
| 27 | MXY | 762 |
| 28 | Cathay Pacific | 758 |
| 29 | United Airlines | 758 |
| 30 | GLO | 752 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 125844 |
| 2 | 🇪🇸 ES | 9464 |
| 3 | 🇦🇺 AU | 8342 |
| 4 | 🇮🇳 IN | 8280 |
| 5 | 🇧🇷 BR | 8240 |
| 6 | 🇨🇦 CA | 7777 |
| 7 | 🇮🇹 IT | 7603 |
| 8 | 🇩🇪 DE | 7529 |
| 9 | 🇬🇧 GB | 6657 |
| 10 | 🇯🇵 JP | 6098 |
| 11 | 🇫🇷 FR | 5808 |
| 12 | 🇨🇴 CO | 4817 |
| 13 | 🇲🇽 MX | 4250 |
| 14 | 🇬🇷 GR | 4147 |
| 15 | 🇳🇴 NO | 3895 |
| 16 | 🇨🇭 CH | 3812 |
| 17 | 🇹🇷 TR | 3429 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2462 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2223 |
| 22 | 🇹🇭 TH | 2140 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1941 |
| 25 | 🇬🇹 GT | 1898 |
| 26 | 🇲🇦 MA | 1510 |
| 27 | 🇲🇪 ME | 1450 |
| 28 | 🇳🇱 NL | 1361 |
| 29 | 🇭🇷 HR | 1332 |
| 30 | 🇲🇴 MO | 1215 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3007 |
| 2 | Denver International Airport |  | US | 2441 |
| 3 | Tokyo International Airport |  | JP | 1960 |
| 4 | Indira Gandhi International Airport |  | IN | 1838 |
| 5 | Harry Reid International Airport |  | US | 1827 |
| 6 | Guaymaral Airport |  | CO | 1799 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1657 |
| 8 | Zurich Airport |  | CH | 1611 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1532 |
| 10 | La Aurora Airport |  | GT | 1470 |
| 11 | Frankfurt am Main International Airport |  | DE | 1400 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1373 |
| 13 | Chicago O'Hare International Airport |  | US | 1354 |
| 14 | Salt Lake City International Airport |  | US | 1312 |
| 15 | El Dorado International Airport |  | CO | 1307 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1266 |
| 17 | Macau International Airport |  | MO | 1215 |
| 18 | Capua Airport |  | IT | 1186 |
| 19 | Congonhas Airport |  | BR | 1176 |
| 20 | Madrid Barajas International Airport |  | ES | 1166 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1147 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1045 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1020 |
| 26 | Charles de Gaulle International Airport |  | FR | 1013 |
| 27 | Bengaluru International Airport |  | IN | 990 |
| 28 | Malpensa International Airport |  | IT | 945 |
| 29 | Ninoy Aquino International Airport |  | PH | 906 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 891 |
| 31 | Barcelona International Airport |  | ES | 883 |
| 32 | Daniel K Inouye International Airport |  | US | 882 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 872 |
| 34 | Tenerife Norte Airport |  | ES | 836 |
| 35 | Seattle-Tacoma International Airport |  | US | 832 |
| 36 | Calgary International Airport |  | CA | 828 |
| 37 | Viracopos International Airport |  | BR | 827 |
| 38 | Scottsdale Airport |  | US | 827 |
| 39 | Amsterdam Airport Schiphol |  | NL | 821 |
| 40 | Oslo Gardermoen Airport |  | NO | 804 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 758 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 531 | 21m | 244 km | 2,235.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 354 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 263 | 26m | 275 km | 1,246.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 262 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 219 | 22m | 55 km | 208.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 196 | 1h 46m | 1,423 km | 4,810.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 195 | 44m | 241 km | 810.0 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 192 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 170 | 1h 16m | 961 km | 2,817.8 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 165 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OOTBB | OOT | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Antwerp International Airport (Deurne) (EBAW) | 2026-07-23 17:01 UTC | 2026-07-23 18:03 UTC | 1h 2m |
| LOOT19 | LOO | Enix Airport (OK51) | Ponca City Regional Airport (KPNC) | 2026-07-23 16:40 UTC | 2026-07-23 17:56 UTC | 1h 16m |
| MAGOO66 | MAG | Sandy Creek Airport (73TX) | Maverick County Memorial International Airport (K5T9) | 2026-07-23 17:32 UTC | 2026-07-23 17:56 UTC | 23m |
| CODE21 | COD | Flying E Ranch Airport (OK16) | Ramey 1 Airport (0OK8) | 2026-07-23 17:34 UTC | 2026-07-23 17:54 UTC | 20m |
| N622TP |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-07-23 17:28 UTC | 2026-07-23 17:54 UTC | 25m |
| BRQ002 | BRQ | Tripoli International Airport (HLLT) | Qaryat Al Karmal Airport (HL64) | 2026-07-23 17:04 UTC | 2026-07-23 17:48 UTC | 44m |
| CXK134 | CXK | Clark Regional Airport (KJVY) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-23 16:54 UTC | 2026-07-23 17:47 UTC | 53m |
| CXK678 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-07-23 16:25 UTC | 2026-07-23 17:44 UTC | 1h 19m |
| N4554J |  | Heritage Field (KPTW) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-23 17:24 UTC | 2026-07-23 17:41 UTC | 16m |
| N92CE |  | Okc Will Rogers International Airport (KOKC) | Cavern City Air Trml Airport (KCNM) | 2026-07-23 16:43 UTC | 2026-07-23 17:37 UTC | 53m |
| LRS1004 | LRS | Juan Santamaria International Airport (MROC) | Tambor Airport (MRTR) | 2026-07-23 17:13 UTC | 2026-07-23 17:34 UTC | 21m |
|  |  | Columbus Airport (KCSG) | Columbus Airport (KCSG) | 2026-07-23 17:33 UTC | 2026-07-23 17:34 UTC | 0m |
| FGD550 | FGD | Prince George Airport (CYXS) | Fraser Lake Airport (CBZ9) | 2026-07-23 17:14 UTC | 2026-07-23 17:33 UTC | 19m |
| JTD651 | JTD | Stockholm-Arlanda Airport (ESSA) | Kasos Airport (LGKS) | 2026-07-23 14:09 UTC | 2026-07-23 17:31 UTC | 3h 22m |
| N861JT |  | Sierraville Dearwater Airport (KO79) | Truckee-Tahoe Airport (KTRK) | 2026-07-23 17:20 UTC | 2026-07-23 17:31 UTC | 10m |
| TJT95SZ | TJT | Marseille Provence Airport (LFML) | Malpensa International Airport (LIMC) | 2026-07-23 16:22 UTC | 2026-07-23 17:30 UTC | 1h 8m |
| KATT84 | KAT | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bay Minette Municipal Airport (K1R8) | 2026-07-23 16:57 UTC | 2026-07-23 17:29 UTC | 32m |
| N429HR |  | Milhous Ranch Airport (79CL) | Milhous Ranch Airport (79CL) | 2026-07-23 16:45 UTC | 2026-07-23 17:28 UTC | 43m |
| FFL830 | FFL | Aurora State Airport (KUAO) | Running Creek Ranch Airport (05ID) | 2026-07-23 16:45 UTC | 2026-07-23 17:27 UTC | 42m |
| MILAN80 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-07-23 17:06 UTC | 2026-07-23 17:26 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
