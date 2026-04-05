# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_10:22:25_UTC-green)

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

**Latest saved flight:** 2026-04-05 10:22:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 10:22:25 UTC

- **17,647** saved flights
- **9,134** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,647** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **223,115.6 tonnes** estimated CO2 emissions
- **12,934,240 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 711 |
| 3 | IndiGo | 506 |
| 4 | EJA | 328 |
| 5 | American Airlines | 323 |
| 6 | Lufthansa | 249 |
| 7 | Southwest Airlines | 247 |
| 8 | ENY | 234 |
| 9 | Vueling | 198 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 179 |
| 12 | All Nippon Airways | 157 |
| 13 | QLK | 154 |
| 14 | Delta Air Lines | 151 |
| 15 | LXJ | 149 |
| 16 | AZU | 131 |
| 17 | VIV | 131 |
| 18 | Swiss International | 130 |
| 19 | Alaska Airlines | 123 |
| 20 | Japan Airlines | 122 |
| 21 | United Airlines | 116 |
| 22 | easyJet | 115 |
| 23 | Avianca | 113 |
| 24 | AEE | 111 |
| 25 | EJU | 111 |
| 26 | AXB | 108 |
| 27 | EDV | 108 |
| 28 | Cathay Pacific | 102 |
| 29 | WIF | 102 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13916 |
| 2 | 🇮🇳 IN | 1542 |
| 3 | 🇪🇸 ES | 1457 |
| 4 | 🇦🇺 AU | 1302 |
| 5 | 🇧🇷 BR | 1002 |
| 6 | 🇯🇵 JP | 970 |
| 7 | 🇩🇪 DE | 918 |
| 8 | 🇨🇴 CO | 905 |
| 9 | 🇮🇹 IT | 812 |
| 10 | 🇨🇦 CA | 780 |
| 11 | 🇬🇧 GB | 684 |
| 12 | 🇫🇷 FR | 638 |
| 13 | 🇲🇽 MX | 609 |
| 14 | 🇬🇷 GR | 493 |
| 15 | 🇨🇭 CH | 465 |
| 16 | 🇲🇾 MY | 405 |
| 17 | 🇳🇿 NZ | 394 |
| 18 | 🇿🇦 ZA | 375 |
| 19 | 🇵🇭 PH | 346 |
| 20 | 🇳🇴 NO | 342 |
| 21 | 🇬🇹 GT | 337 |
| 22 | 🇹🇷 TR | 327 |
| 23 | 🇰🇷 KR | 321 |
| 24 | 🇹🇭 TH | 250 |
| 25 | 🇵🇱 PL | 248 |
| 26 | 🇲🇦 MA | 215 |
| 27 | 🇮🇩 ID | 198 |
| 28 | 🇧🇸 BS | 191 |
| 29 | 🇲🇴 MO | 188 |
| 30 | 🇲🇪 ME | 183 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 420 |
| 2 | El Dorado International Airport |  | CO | 343 |
| 3 | Tokyo International Airport |  | JP | 331 |
| 4 | Denver International Airport |  | US | 327 |
| 5 | Indira Gandhi International Airport |  | IN | 323 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Harry Reid International Airport |  | US | 232 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 231 |
| 9 | Frankfurt am Main International Airport |  | DE | 220 |
| 10 | Zurich Airport |  | CH | 213 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 190 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 13 | Macau International Airport |  | MO | 188 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 15 | Guaymaral Airport |  | CO | 182 |
| 16 | Chicago O'Hare International Airport |  | US | 172 |
| 17 | Bengaluru International Airport |  | IN | 172 |
| 18 | Madrid Barajas International Airport |  | ES | 166 |
| 19 | Charlotte/Douglas International Airport |  | US | 165 |
| 20 | Ninoy Aquino International Airport |  | PH | 158 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 22 | Congonhas Airport |  | BR | 154 |
| 23 | Tenerife Norte Airport |  | ES | 153 |
| 24 | Daniel K Inouye International Airport |  | US | 144 |
| 25 | Salt Lake City International Airport |  | US | 142 |
| 26 | Kuala Lumpur International Airport |  | MY | 142 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 28 | Malpensa International Airport |  | IT | 137 |
| 29 | Reno/Tahoe International Airport |  | US | 136 |
| 30 | Vitoria/Foronda Airport |  | ES | 135 |
| 31 | Charles de Gaulle International Airport |  | FR | 130 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 33 | Miami International Airport |  | US | 123 |
| 34 | Barcelona International Airport |  | ES | 123 |
| 35 | Pune Airport |  | IN | 118 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 117 |
| 38 | Seattle-Tacoma International Airport |  | US | 115 |
| 39 | General Edward Lawrence Logan International Airport |  | US | 112 |
| 40 | O. R. Tambo International Airport |  | ZA | 112 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 84 | 1h 8m | 706 km | 1,022.7 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 63 | 29m | 304 km | 330.3 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 52 | 1h 44m | 1,156 km | 1,037.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 52 | 31m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 51 | 1h 27m | 910 km | 800.3 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 49 | 16m | 206 km | 174.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 43 | 28m | 275 km | 203.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 40 | 19m | 165 km | 113.8 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 39 | 1h 11m | 770 km | 518.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 38 | 30m | 369 km | 241.9 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 36 | 54m | 546 km | 338.9 t |
| 19 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 33 | 1h 43m | 1,423 km | 809.9 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 32 | 23m | 252 km | 138.9 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 32 | 46m | 452 km | 249.4 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 30 | 11m | 127 km | 65.7 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 26 | 20m | 250 km | 112.3 t |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JST713 | JST | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 2026-04-05 09:47 UTC | 2026-04-05 10:22 UTC | 35m |
| GTI8522 | GTI | Incheon International Airport (RKSI) | Macau International Airport (VMMC) | 2026-04-05 02:24 UTC | 2026-04-05 10:17 UTC | 7h 53m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-04 19:17 UTC | 2026-04-05 10:02 UTC | 14h 44m |
| CRK399 | CRK | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-04-05 02:12 UTC | 2026-04-05 09:44 UTC | 7h 31m |
| HBZWD | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-04-05 09:19 UTC | 2026-04-05 09:42 UTC | 22m |
| SFJ85 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-05 08:21 UTC | 2026-04-05 09:35 UTC | 1h 13m |
| HBPHG | HBP | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-04-05 09:19 UTC | 2026-04-05 09:33 UTC | 14m |
| RMB1 | RMB | Geneva Cointrin International Airport (LSGG) | Decimomannu Airport (LIED) | 2026-04-05 08:29 UTC | 2026-04-05 09:32 UTC | 1h 2m |
| VOE3359 | VOE | Malaga Airport (LEMG) | San Sebastian Airport (LESO) | 2026-04-05 08:28 UTC | 2026-04-05 09:31 UTC | 1h 3m |
| AIC5NQ | Air India | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-04-05 09:10 UTC | 2026-04-05 09:29 UTC | 18m |
| JAL669 | Japan Airlines | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-05 08:18 UTC | 2026-04-05 09:26 UTC | 1h 7m |
| AWQ176 | AWQ | Soekarno-Hatta International Airport (WIII) | WIAT (WIAT) | 2026-04-05 09:12 UTC | 2026-04-05 09:24 UTC | 12m |
| VOE1445 | VOE | Barcelona International Airport (LEBL) | Olbia / Costa Smeralda Airport (LIEO) | 2026-04-05 08:30 UTC | 2026-04-05 09:24 UTC | 54m |
| ANA786 | All Nippon Airways | Osaka International Airport (RJOO) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-05 08:44 UTC | 2026-04-05 09:20 UTC | 35m |
| KAL1827 | Korean Air | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-05 08:53 UTC | 2026-04-05 09:19 UTC | 26m |
| AFR35BQ | Air France | Charles de Gaulle International Airport (LFPG) | Linate Airport (LIML) | 2026-04-05 08:13 UTC | 2026-04-05 09:19 UTC | 1h 5m |
| PSSIU | PSS | Nascimento I Airport (SDNI) | Fazenda Sao Joao Airport (SSZT) | 2026-04-05 08:54 UTC | 2026-04-05 09:19 UTC | 24m |
| WMT5CB | WMT | Memmingen Allgau Airport (EDJA) | Kukes Airport (LAKU) | 2026-04-05 07:57 UTC | 2026-04-05 09:17 UTC | 1h 19m |
| EZY89HE | easyJet | Bristol International Airport (EGGD) | La Gomera Airport (GCGM) | 2026-04-05 05:30 UTC | 2026-04-05 09:16 UTC | 3h 46m |
| RYR2778 | Ryanair | Thessaloniki Macedonia International Airport (LGTS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-05 07:35 UTC | 2026-04-05 09:15 UTC | 1h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
