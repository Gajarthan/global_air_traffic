# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_13:33:29_UTC-green)

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

**Latest saved flight:** 2026-08-17 13:33:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 13:33:29 UTC

- **208,032** saved flights
- **66,108** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **208,032** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,502,082.5 tonnes** estimated CO2 emissions
- **145,048,259 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8219 |
| 2 | SkyWest Airlines | 7462 |
| 3 | EJA | 4041 |
| 4 | IndiGo | 3563 |
| 5 | American Airlines | 3456 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2669 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1962 |
| 10 | AZU | 1880 |
| 11 | Lufthansa | 1759 |
| 12 | Vueling | 1729 |
| 13 | WIF | 1677 |
| 14 | LXJ | 1644 |
| 15 | easyJet | 1436 |
| 16 | Swiss International | 1386 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1307 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1268 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1145 |
| 24 | GLO | 1122 |
| 25 | Air France | 1116 |
| 26 | PGT | 1115 |
| 27 | AEE | 1064 |
| 28 | JetBlue | 1064 |
| 29 | WMT | 1053 |
| 30 | Wizz Air | 1028 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176165 |
| 2 | 🇪🇸 ES | 13311 |
| 3 | 🇧🇷 BR | 11919 |
| 4 | 🇦🇺 AU | 11745 |
| 5 | 🇨🇦 CA | 11473 |
| 6 | 🇮🇳 IN | 11119 |
| 7 | 🇮🇹 IT | 10876 |
| 8 | 🇩🇪 DE | 10289 |
| 9 | 🇬🇧 GB | 9693 |
| 10 | 🇯🇵 JP | 8643 |
| 11 | 🇨🇴 CO | 8262 |
| 12 | 🇫🇷 FR | 8239 |
| 13 | 🇬🇷 GR | 6131 |
| 14 | 🇹🇷 TR | 5917 |
| 15 | 🇲🇽 MX | 5844 |
| 16 | 🇨🇭 CH | 5548 |
| 17 | 🇳🇴 NO | 5191 |
| 18 | 🇲🇾 MY | 3593 |
| 19 | 🇿🇦 ZA | 3500 |
| 20 | 🇵🇱 PL | 3429 |
| 21 | 🇹🇭 TH | 3343 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2771 |
| 24 | 🇬🇹 GT | 2665 |
| 25 | 🇰🇷 KR | 2544 |
| 26 | 🇭🇷 HR | 2234 |
| 27 | 🇲🇦 MA | 2101 |
| 28 | 🇳🇱 NL | 1850 |
| 29 | 🇲🇪 ME | 1765 |
| 30 | 🇮🇩 ID | 1723 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4366 |
| 2 | Denver International Airport |  | US | 3395 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2529 |
| 5 | Guaymaral Airport |  | CO | 2501 |
| 6 | Harry Reid International Airport |  | US | 2347 |
| 7 | Zurich Airport |  | CH | 2170 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2169 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2152 |
| 10 | La Aurora Airport |  | GT | 2027 |
| 11 | Chicago O'Hare International Airport |  | US | 1922 |
| 12 | El Dorado International Airport |  | CO | 1897 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1857 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1735 |
| 16 | Frankfurt am Main International Airport |  | DE | 1715 |
| 17 | Madrid Barajas International Airport |  | ES | 1634 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1580 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1576 |
| 20 | Capua Airport |  | IT | 1574 |
| 21 | Macau International Airport |  | MO | 1545 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1513 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1467 |
| 24 | Malpensa International Airport |  | IT | 1444 |
| 25 | Charles de Gaulle International Airport |  | FR | 1429 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1313 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1285 |
| 30 | Bengaluru International Airport |  | IN | 1284 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Barcelona International Airport |  | ES | 1245 |
| 33 | Seattle-Tacoma International Airport |  | US | 1238 |
| 34 | Viracopos International Airport |  | BR | 1205 |
| 35 | Calgary International Airport |  | CA | 1175 |
| 36 | Oslo Gardermoen Airport |  | NO | 1151 |
| 37 | Vitoria/Foronda Airport |  | ES | 1147 |
| 38 | Reno/Tahoe International Airport |  | US | 1143 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1114 |
| 40 | Daniel K Inouye International Airport |  | US | 1110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1028 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 348 | 27m | 275 km | 1,649.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 344 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 305 | 44m | 241 km | 1,266.9 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 304 | 1h 49m | 1,423 km | 7,460.6 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 265 | 24m | 218 km | 998.4 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 258 | 19m | 99 km | 441.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 255 | 27m | 215 km | 944.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 249 | 1h 37m | 1,156 km | 4,967.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 238 | 19m | 144 km | 592.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 228 | 28m | 152 km | 595.8 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N397BC |  | Huntingburg Airport (KHNB) | CO86 (CO86) | 2026-08-17 11:06 UTC | 2026-08-17 13:33 UTC | 2h 26m |
| N787MF |  | Orlando Executive Airport (KORL) | Orlando Apopka Airport (KX04) | 2026-08-17 12:36 UTC | 2026-08-17 13:32 UTC | 56m |
| N215BB |  | Hilton Head Airport (KHXD) | Teterboro Airport (KTEB) | 2026-08-17 12:00 UTC | 2026-08-17 13:32 UTC | 1h 31m |
| LFA689 | LFA | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-08-17 13:28 UTC | 2026-08-17 13:30 UTC | 2m |
| CHH470 | CHH | Melsbroek Air Base (EBMB) | Tunoshna Airport (UUDL) | 2026-08-17 10:32 UTC | 2026-08-17 13:29 UTC | 2h 56m |
| N54947 |  | Maryland Airport (K2W5) | Maryland Airport (K2W5) | 2026-08-17 13:04 UTC | 2026-08-17 13:29 UTC | 24m |
| DBT512 | DBT | Malaga Airport (LEMG) | Sevilla Airport (LEZL) | 2026-08-17 13:03 UTC | 2026-08-17 13:28 UTC | 24m |
| VTOMM | VTO | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-08-17 13:11 UTC | 2026-08-17 13:28 UTC | 17m |
| N313TW |  | Newton-City-County Airport (KEWK) | Taylor Airport (SN46) | 2026-08-17 13:15 UTC | 2026-08-17 13:27 UTC | 12m |
| HAWK235 | HAW | Kingsville Nas Airport (KNQI) | Duval County Ranch Company Airport (28TA) | 2026-08-17 13:10 UTC | 2026-08-17 13:23 UTC | 12m |
| DRAGO06 | DRA | Cannes-Mandelieu Airport (LFMD) | Cuneo / Levaldigi Airport (LIMZ) | 2026-08-17 12:45 UTC | 2026-08-17 13:20 UTC | 34m |
| N98840 |  | Grand Prairie Municipal Airport (KGPM) | 54OK (54OK) | 2026-08-17 11:35 UTC | 2026-08-17 13:20 UTC | 1h 45m |
| N747DW |  | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-08-17 12:48 UTC | 2026-08-17 13:16 UTC | 28m |
| N434MG |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-17 12:40 UTC | 2026-08-17 13:14 UTC | 34m |
| PRDBS | PRD | Congonhas Airport (SBSP) | Araxa Airport (SBAX) | 2026-08-17 12:26 UTC | 2026-08-17 13:12 UTC | 46m |
| SPSMH | SPS | Poznań-Kobylnica Airport (EPPK) | Poznań-Kobylnica Airport (EPPK) | 2026-08-17 13:02 UTC | 2026-08-17 13:12 UTC | 10m |
| N120RP |  | St Simons Island Airport (KSSI) | Dekalb-Peachtree Airport (KPDK) | 2026-08-17 12:07 UTC | 2026-08-17 13:11 UTC | 1h 4m |
| LRS5790 | LRS | Juan Santamaria International Airport (MROC) | Guapiles Airport (MRGP) | 2026-08-17 12:58 UTC | 2026-08-17 13:10 UTC | 11m |
| TGTUY | TGT | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-17 12:43 UTC | 2026-08-17 13:07 UTC | 24m |
| N999VP |  | Vogen Airport (IS41) | Vogen Airport (IS41) | 2026-08-17 12:32 UTC | 2026-08-17 13:02 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
