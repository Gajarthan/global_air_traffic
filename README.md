# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_04:30:33_UTC-green)

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

**Latest saved flight:** 2026-07-13 04:30:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-13 04:30:33 UTC

- **139,653** saved flights
- **47,043** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **139,653** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,677,067.8 tonnes** estimated CO2 emissions
- **97,221,320 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5686 |
| 2 | SkyWest Airlines | 5120 |
| 3 | EJA | 2755 |
| 4 | IndiGo | 2561 |
| 5 | American Airlines | 2211 |
| 6 | Southwest Airlines | 2104 |
| 7 | ENY | 1743 |
| 8 | Delta Air Lines | 1656 |
| 9 | Lufthansa | 1423 |
| 10 | LATAM Airlines | 1283 |
| 11 | Vueling | 1206 |
| 12 | AZU | 1201 |
| 13 | WIF | 1200 |
| 14 | LXJ | 1072 |
| 15 | AXM | 1045 |
| 16 | Swiss International | 993 |
| 17 | easyJet | 907 |
| 18 | All Nippon Airways | 899 |
| 19 | Alaska Airlines | 879 |
| 20 | QLK | 876 |
| 21 | EJU | 861 |
| 22 | VIV | 769 |
| 23 | AEE | 751 |
| 24 | CXK | 750 |
| 25 | Air France | 748 |
| 26 | JetBlue | 735 |
| 27 | United Airlines | 731 |
| 28 | Cathay Pacific | 729 |
| 29 | MXY | 726 |
| 30 | GLO | 715 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 120045 |
| 2 | 🇪🇸 ES | 9165 |
| 3 | 🇮🇳 IN | 8024 |
| 4 | 🇦🇺 AU | 7988 |
| 5 | 🇧🇷 BR | 7882 |
| 6 | 🇨🇦 CA | 7330 |
| 7 | 🇮🇹 IT | 7292 |
| 8 | 🇩🇪 DE | 7281 |
| 9 | 🇬🇧 GB | 6335 |
| 10 | 🇯🇵 JP | 5875 |
| 11 | 🇫🇷 FR | 5559 |
| 12 | 🇨🇴 CO | 4416 |
| 13 | 🇲🇽 MX | 4054 |
| 14 | 🇬🇷 GR | 3979 |
| 15 | 🇳🇴 NO | 3754 |
| 16 | 🇨🇭 CH | 3620 |
| 17 | 🇹🇷 TR | 3278 |
| 18 | 🇲🇾 MY | 2714 |
| 19 | 🇵🇱 PL | 2336 |
| 20 | 🇿🇦 ZA | 2284 |
| 21 | 🇳🇿 NZ | 2140 |
| 22 | 🇹🇭 TH | 2105 |
| 23 | 🇰🇷 KR | 2010 |
| 24 | 🇵🇭 PH | 1899 |
| 25 | 🇬🇹 GT | 1848 |
| 26 | 🇲🇦 MA | 1465 |
| 27 | 🇲🇪 ME | 1386 |
| 28 | 🇳🇱 NL | 1309 |
| 29 | 🇭🇷 HR | 1262 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2886 |
| 2 | Denver International Airport |  | US | 2341 |
| 3 | Tokyo International Airport |  | JP | 1907 |
| 4 | Indira Gandhi International Airport |  | IN | 1774 |
| 5 | Harry Reid International Airport |  | US | 1744 |
| 6 | Guaymaral Airport |  | CO | 1701 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1611 |
| 8 | Zurich Airport |  | CH | 1553 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1466 |
| 10 | La Aurora Airport |  | GT | 1428 |
| 11 | Frankfurt am Main International Airport |  | DE | 1373 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1335 |
| 13 | Chicago O'Hare International Airport |  | US | 1315 |
| 14 | Salt Lake City International Airport |  | US | 1244 |
| 15 | El Dorado International Airport |  | CO | 1239 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1199 |
| 17 | Macau International Airport |  | MO | 1188 |
| 18 | Capua Airport |  | IT | 1147 |
| 19 | Madrid Barajas International Airport |  | ES | 1137 |
| 20 | Congonhas Airport |  | BR | 1122 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1120 |
| 22 | Kuala Lumpur International Airport |  | MY | 1052 |
| 23 | Charlotte/Douglas International Airport |  | US | 1022 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1008 |
| 25 | Charles de Gaulle International Airport |  | FR | 991 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 967 |
| 27 | Bengaluru International Airport |  | IN | 961 |
| 28 | Malpensa International Airport |  | IT | 906 |
| 29 | Ninoy Aquino International Airport |  | PH | 885 |
| 30 | Daniel K Inouye International Airport |  | US | 856 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 854 |
| 32 | Barcelona International Airport |  | ES | 851 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 820 |
| 34 | Tenerife Norte Airport |  | ES | 816 |
| 35 | Calgary International Airport |  | CA | 804 |
| 36 | Viracopos International Airport |  | BR | 798 |
| 37 | Seattle-Tacoma International Airport |  | US | 795 |
| 38 | Scottsdale Airport |  | US | 793 |
| 39 | Amsterdam Airport Schiphol |  | NL | 783 |
| 40 | Vitoria/Foronda Airport |  | ES | 777 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 717 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 506 | 21m | 244 km | 2,130.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 343 | 24m | 225 km | 1,330.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 342 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 331 | 1h 9m | 770 km | 4,397.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 190 | 26m | 215 km | 703.7 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 186 | 20m | 99 km | 318.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 184 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 168 | 18m | 144 km | 417.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 157 | 1h 38m | 1,156 km | 3,132.1 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 154 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 83B |  | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-13 03:57 UTC | 2026-07-13 04:30 UTC | 33m |
| YUJ | YUJ | Brisbane Archerfield Airport (YBAF) | Sunshine Coast Airport (YBMC) | 2026-07-13 03:47 UTC | 2026-07-13 04:28 UTC | 40m |
| N45FS |  | Centennial Airport (KAPA) | Leach Airport (K1V8) | 2026-07-13 03:50 UTC | 2026-07-13 04:14 UTC | 24m |
| IGO7419 | IndiGo | VGCM (VGCM) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-07-13 03:04 UTC | 2026-07-13 03:59 UTC | 54m |
| VYR686 | VYR | Springdale Municipal Airport (KASG) | Mc Elroy Airfield (K20V) | 2026-07-13 02:22 UTC | 2026-07-13 03:52 UTC | 1h 29m |
| SCU8 | SCU | Kansas City Downtown/Wheeler Field (KMKC) | Barcus Field (95OK) | 2026-07-13 02:10 UTC | 2026-07-13 03:48 UTC | 1h 38m |
| N470X |  | Lewiston/Nez Perce County Airport (KLWS) | MT97 (MT97) | 2026-07-13 02:52 UTC | 2026-07-13 03:36 UTC | 44m |
| OGN508 | OGN | Wellington International Airport (NZWN) | Picton Aerodrome (NZPN) | 2026-07-13 03:14 UTC | 2026-07-13 03:32 UTC | 18m |
| FFT2816 | FFT | Jacksonville International Airport (KJAX) | Philadelphia International Airport (KPHL) | 2026-07-13 01:53 UTC | 2026-07-13 03:32 UTC | 1h 38m |
| ANA375 | All Nippon Airways | Tokyo International Airport (RJTT) | Monbetsu Airport (RJEB) | 2026-07-13 02:04 UTC | 2026-07-13 03:31 UTC | 1h 27m |
| EEA | EEA | Brisbane Archerfield Airport (YBAF) | Sunshine Coast Airport (YBMC) | 2026-07-13 02:51 UTC | 2026-07-13 03:28 UTC | 37m |
| UBG183 | UBG | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-07-13 02:40 UTC | 2026-07-13 03:27 UTC | 46m |
| 8M2 |  | Cessnock Airport (YCNK) | Young Airport (YYNG) | 2026-07-13 02:53 UTC | 2026-07-13 03:25 UTC | 32m |
| KGJ | KGJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-07-13 02:55 UTC | 2026-07-13 03:22 UTC | 26m |
| JBU810 | JetBlue | Jacksonville International Airport (KJAX) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-13 00:51 UTC | 2026-07-13 03:20 UTC | 2h 29m |
| PGT1847 | PGT | Tbilisi International Airport (UGTB) | Imsik Airport (LTBV) | 2026-07-13 01:08 UTC | 2026-07-13 03:20 UTC | 2h 12m |
| CSI571 | CSI | Albuquerque International Sunport Airport (KABQ) | Jicarilla Apache Nation Airport (K24N) | 2026-07-13 02:56 UTC | 2026-07-13 03:20 UTC | 23m |
| QLK386D | QLK | Brisbane International Airport (YBBN) | Grenfell Airport (YGNF) | 2026-07-13 01:49 UTC | 2026-07-13 03:20 UTC | 1h 30m |
| VOI3316 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | General Jose Maria Yanez International Airport (MMGM) | 2026-07-13 02:10 UTC | 2026-07-13 03:19 UTC | 1h 8m |
| N482WT |  | Millard Airport (KMLE) | Iowa City Municipal Airport (KIOW) | 2026-07-13 01:56 UTC | 2026-07-13 03:19 UTC | 1h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
