# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_19:52:39_UTC-green)

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

**Latest saved flight:** 2026-06-15 19:52:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-15 19:52:39 UTC

- **111,361** saved flights
- **38,829** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **111,361** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,361,837.5 tonnes** estimated CO2 emissions
- **78,947,104 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4600 |
| 2 | SkyWest Airlines | 4166 |
| 3 | IndiGo | 2180 |
| 4 | EJA | 2159 |
| 5 | American Airlines | 1757 |
| 6 | Southwest Airlines | 1665 |
| 7 | ENY | 1383 |
| 8 | Delta Air Lines | 1319 |
| 9 | Lufthansa | 1257 |
| 10 | Vueling | 1022 |
| 11 | WIF | 985 |
| 12 | LATAM Airlines | 982 |
| 13 | AXM | 936 |
| 14 | AZU | 922 |
| 15 | LXJ | 851 |
| 16 | Swiss International | 799 |
| 17 | All Nippon Airways | 774 |
| 18 | Alaska Airlines | 756 |
| 19 | QLK | 730 |
| 20 | easyJet | 720 |
| 21 | EJU | 708 |
| 22 | Cathay Pacific | 659 |
| 23 | AEE | 629 |
| 24 | VIV | 623 |
| 25 | Air France | 622 |
| 26 | United Airlines | 622 |
| 27 | MXY | 594 |
| 28 | CXK | 584 |
| 29 | AXB | 547 |
| 30 | GLO | 545 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 93714 |
| 2 | 🇪🇸 ES | 7648 |
| 3 | 🇮🇳 IN | 6871 |
| 4 | 🇦🇺 AU | 6606 |
| 5 | 🇧🇷 BR | 6150 |
| 6 | 🇮🇹 IT | 6001 |
| 7 | 🇩🇪 DE | 5957 |
| 8 | 🇨🇦 CA | 5847 |
| 9 | 🇯🇵 JP | 5035 |
| 10 | 🇬🇧 GB | 4791 |
| 11 | 🇫🇷 FR | 4447 |
| 12 | 🇨🇴 CO | 3783 |
| 13 | 🇲🇽 MX | 3304 |
| 14 | 🇬🇷 GR | 3169 |
| 15 | 🇳🇴 NO | 3081 |
| 16 | 🇨🇭 CH | 2852 |
| 17 | 🇲🇾 MY | 2418 |
| 18 | 🇹🇷 TR | 2218 |
| 19 | 🇿🇦 ZA | 1895 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1836 |
| 22 | 🇵🇱 PL | 1827 |
| 23 | 🇳🇿 NZ | 1822 |
| 24 | 🇵🇭 PH | 1621 |
| 25 | 🇬🇹 GT | 1592 |
| 26 | 🇲🇦 MA | 1227 |
| 27 | 🇲🇴 MO | 1151 |
| 28 | 🇲🇪 ME | 1091 |
| 29 | 🇳🇱 NL | 1084 |
| 30 | 🇭🇷 HR | 970 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2371 |
| 2 | Denver International Airport |  | US | 1893 |
| 3 | Tokyo International Airport |  | JP | 1669 |
| 4 | Indira Gandhi International Airport |  | IN | 1493 |
| 5 | Guaymaral Airport |  | CO | 1406 |
| 6 | Harry Reid International Airport |  | US | 1402 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1382 |
| 8 | Zurich Airport |  | CH | 1252 |
| 9 | Frankfurt am Main International Airport |  | DE | 1230 |
| 10 | La Aurora Airport |  | GT | 1224 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1197 |
| 12 | Macau International Airport |  | MO | 1151 |
| 13 | El Dorado International Airport |  | CO | 1138 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1117 |
| 15 | Chicago O'Hare International Airport |  | US | 1107 |
| 16 | Madrid Barajas International Airport |  | ES | 973 |
| 17 | Capua Airport |  | IT | 968 |
| 18 | Salt Lake City International Airport |  | US | 946 |
| 19 | Kuala Lumpur International Airport |  | MY | 941 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 938 |
| 21 | Congonhas Airport |  | BR | 856 |
| 22 | Charlotte/Douglas International Airport |  | US | 855 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 836 |
| 24 | Charles de Gaulle International Airport |  | FR | 834 |
| 25 | Bengaluru International Airport |  | IN | 829 |
| 26 | Malpensa International Airport |  | IT | 812 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 756 |
| 28 | Ninoy Aquino International Airport |  | PH | 748 |
| 29 | Daniel K Inouye International Airport |  | US | 738 |
| 30 | Tenerife Norte Airport |  | ES | 734 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 728 |
| 32 | Barcelona International Airport |  | ES | 727 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 711 |
| 34 | Don Mueang International Airport |  | TH | 669 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 662 |
| 37 | Calgary International Airport |  | CA | 657 |
| 38 | Norman Y Mineta San Jose International Airport |  | US | 640 |
| 39 | Seattle-Tacoma International Airport |  | US | 640 |
| 40 | Viracopos International Airport |  | BR | 630 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 583 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 406 | 21m | 244 km | 1,709.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 287 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 272 | 1h 25m | 910 km | 4,268.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 262 | 1h 10m | 770 km | 3,480.5 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 224 | 26m | 275 km | 1,061.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 162 | 27m | 215 km | 600.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 160 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 153 | 27m | 152 km | 399.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 151 | 31m | 369 km | 961.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 143 | 20m | 250 km | 617.7 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 142 | 44m | 241 km | 589.8 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 134 | 1h 1m | 695 km | 1,606.3 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 125 | 12m | - | - |
| 29 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N487BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-06-15 19:00 UTC | 2026-06-15 19:52 UTC | 52m |
| FAM3527 | FAM | Santa Lucia Air Force Base (MMSM) | Santa Lucia Air Force Base (MMSM) | 2026-06-15 19:13 UTC | 2026-06-15 19:49 UTC | 35m |
| PPBLV | PPB | Linhares Airport (SNLN) | Eurico de Aguiar Salles Airport (SBVT) | 2026-06-15 19:21 UTC | 2026-06-15 19:46 UTC | 25m |
| RYS3061 | RYS | Katowice International Airport (EPKT) | Aktion National Airport (LGPZ) | 2026-06-15 18:08 UTC | 2026-06-15 19:42 UTC | 1h 34m |
| N4922D |  | Montgomery-Gibbs Executive Airport (KMYF) | Mc Clellan-Palomar Airport (KCRQ) | 2026-06-15 18:49 UTC | 2026-06-15 19:40 UTC | 50m |
| 145TX |  | Austin-Bergstrom International Airport (KAUS) | Austin-Bergstrom International Airport (KAUS) | 2026-06-15 18:59 UTC | 2026-06-15 19:39 UTC | 40m |
| N69F |  | Newark Liberty International Airport (KEWR) | Teterboro Airport (KTEB) | 2026-06-15 19:10 UTC | 2026-06-15 19:33 UTC | 23m |
| N39HF |  | Newark Liberty International Airport (KEWR) | Westchester County Airport (KHPN) | 2026-06-15 19:07 UTC | 2026-06-15 19:29 UTC | 22m |
| JNX105 | JNX | Willow Springs Ranch Airport (1AZ8) | Kingman Airport (KIGM) | 2026-06-15 19:04 UTC | 2026-06-15 19:29 UTC | 25m |
| GSM650 | GSM | Savannah/Hilton Head International Airport (KSAV) | Robert F Swinnie Airport (KPHH) | 2026-06-15 19:07 UTC | 2026-06-15 19:27 UTC | 20m |
| N6163F |  | Wade Airport (56LL) | De Kalb Taylor Municipal Airport (KDKB) | 2026-06-15 19:14 UTC | 2026-06-15 19:21 UTC | 6m |
|  |  | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-06-15 17:45 UTC | 2026-06-15 19:21 UTC | 1h 36m |
| FORGE77 | FOR | Joint Base Andrews Airport (KADW) | Laurence G Hanscom Field (KBED) | 2026-06-15 16:16 UTC | 2026-06-15 19:20 UTC | 3h 4m |
| CXK487 | CXK | Ruder Airport (59IL) | Ruder Airport (59IL) | 2026-06-15 19:18 UTC | 2026-06-15 19:19 UTC | 0m |
| N9454F |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-15 19:06 UTC | 2026-06-15 19:19 UTC | 12m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-06-15 18:56 UTC | 2026-06-15 19:13 UTC | 16m |
| N197WW |  | Québec City Jean Lesage International Airport (CYQB) | Québec City Jean Lesage International Airport (CYQB) | 2026-06-15 18:58 UTC | 2026-06-15 19:12 UTC | 13m |
| MSR782 | EgyptAir | Manchester Airport (EGCC) | HE12 (HE12) | 2026-06-15 15:01 UTC | 2026-06-15 19:12 UTC | 4h 10m |
| N137TM |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-06-15 18:58 UTC | 2026-06-15 19:09 UTC | 10m |
| EJA977 | EJA | Stag Air Park (7NC1) | Westchester County Airport (KHPN) | 2026-06-15 17:55 UTC | 2026-06-15 19:07 UTC | 1h 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
