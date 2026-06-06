# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_16:34:50_UTC-green)

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

**Latest saved flight:** 2026-06-06 16:34:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 16:34:50 UTC

- **104,169** saved flights
- **36,764** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **104,169** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,273,105.0 tonnes** estimated CO2 emissions
- **73,803,191 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4281 |
| 2 | SkyWest Airlines | 3905 |
| 3 | IndiGo | 2087 |
| 4 | EJA | 1987 |
| 5 | American Airlines | 1678 |
| 6 | Southwest Airlines | 1570 |
| 7 | ENY | 1300 |
| 8 | Delta Air Lines | 1232 |
| 9 | Lufthansa | 1200 |
| 10 | Vueling | 964 |
| 11 | LATAM Airlines | 922 |
| 12 | WIF | 914 |
| 13 | AXM | 897 |
| 14 | AZU | 836 |
| 15 | LXJ | 783 |
| 16 | Swiss International | 753 |
| 17 | All Nippon Airways | 734 |
| 18 | Alaska Airlines | 723 |
| 19 | QLK | 697 |
| 20 | easyJet | 675 |
| 21 | EJU | 655 |
| 22 | Cathay Pacific | 622 |
| 23 | AEE | 603 |
| 24 | Air France | 598 |
| 25 | VIV | 597 |
| 26 | United Airlines | 575 |
| 27 | MXY | 563 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 514 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87537 |
| 2 | 🇪🇸 ES | 7175 |
| 3 | 🇮🇳 IN | 6589 |
| 4 | 🇦🇺 AU | 6310 |
| 5 | 🇧🇷 BR | 5695 |
| 6 | 🇩🇪 DE | 5608 |
| 7 | 🇮🇹 IT | 5538 |
| 8 | 🇨🇦 CA | 5417 |
| 9 | 🇯🇵 JP | 4819 |
| 10 | 🇬🇧 GB | 4398 |
| 11 | 🇫🇷 FR | 4133 |
| 12 | 🇨🇴 CO | 3592 |
| 13 | 🇲🇽 MX | 3119 |
| 14 | 🇬🇷 GR | 2966 |
| 15 | 🇳🇴 NO | 2896 |
| 16 | 🇨🇭 CH | 2663 |
| 17 | 🇲🇾 MY | 2295 |
| 18 | 🇹🇷 TR | 1984 |
| 19 | 🇿🇦 ZA | 1804 |
| 20 | 🇳🇿 NZ | 1744 |
| 21 | 🇹🇭 TH | 1723 |
| 22 | 🇰🇷 KR | 1721 |
| 23 | 🇵🇱 PL | 1688 |
| 24 | 🇵🇭 PH | 1531 |
| 25 | 🇬🇹 GT | 1519 |
| 26 | 🇲🇦 MA | 1151 |
| 27 | 🇲🇴 MO | 1098 |
| 28 | 🇳🇱 NL | 1025 |
| 29 | 🇲🇪 ME | 988 |
| 30 | 🇭🇷 HR | 911 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2263 |
| 2 | Denver International Airport |  | US | 1780 |
| 3 | Tokyo International Airport |  | JP | 1599 |
| 4 | Indira Gandhi International Airport |  | IN | 1429 |
| 5 | Harry Reid International Airport |  | US | 1334 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1325 |
| 7 | Guaymaral Airport |  | CO | 1302 |
| 8 | Frankfurt am Main International Airport |  | DE | 1197 |
| 9 | Zurich Airport |  | CH | 1183 |
| 10 | La Aurora Airport |  | GT | 1168 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1124 |
| 12 | El Dorado International Airport |  | CO | 1098 |
| 13 | Macau International Airport |  | MO | 1098 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1052 |
| 15 | Chicago O'Hare International Airport |  | US | 1044 |
| 16 | Madrid Barajas International Airport |  | ES | 906 |
| 17 | Kuala Lumpur International Airport |  | MY | 899 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 890 |
| 19 | Salt Lake City International Airport |  | US | 881 |
| 20 | Capua Airport |  | IT | 871 |
| 21 | Charlotte/Douglas International Airport |  | US | 809 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 794 |
| 24 | Bengaluru International Airport |  | IN | 792 |
| 25 | Congonhas Airport |  | BR | 791 |
| 26 | Malpensa International Airport |  | IT | 783 |
| 27 | Daniel K Inouye International Airport |  | US | 713 |
| 28 | Tenerife Norte Airport |  | ES | 708 |
| 29 | Ninoy Aquino International Airport |  | PH | 699 |
| 30 | Barcelona International Airport |  | ES | 685 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 675 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 669 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 669 |
| 34 | Amsterdam Airport Schiphol |  | NL | 635 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 627 |
| 37 | Calgary International Airport |  | CA | 617 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 600 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 590 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 537 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 381 | 21m | 244 km | 1,604.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 274 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 263 | 14m | 114 km | 515.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 206 | 26m | 275 km | 976.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 160 | 20m | 99 km | 274.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 144 | 31m | 369 km | 916.6 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 135 | 18m | 144 km | 335.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 121 | 1h 43m | 1,423 km | 2,969.5 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 120 | 1h 52m | 1,304 km | 2,699.7 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N475RC |  | Pleasant Valley Airstrip (24AZ) | Pleasant Valley Airstrip (24AZ) | 2026-06-06 16:24 UTC | 2026-06-06 16:34 UTC | 10m |
| AHK769 | AHK | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-06-06 13:57 UTC | 2026-06-06 16:31 UTC | 2h 33m |
| N656BB |  | Mathews Memorial Airport (K8C4) | Washington Municipal Airport (KAWG) | 2026-06-06 15:37 UTC | 2026-06-06 16:29 UTC | 51m |
| N485LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-06-06 16:07 UTC | 2026-06-06 16:26 UTC | 19m |
| N618DH |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-06-06 15:47 UTC | 2026-06-06 16:24 UTC | 37m |
| N7079F |  | Payson Airport (KPAN) | Payson Airport (KPAN) | 2026-06-06 16:08 UTC | 2026-06-06 16:23 UTC | 15m |
| ERU876 | ERU | Deland Municipal-Sidney H Taylor Field (KDED) | North Exuma Airport (85FA) | 2026-06-06 16:21 UTC | 2026-06-06 16:23 UTC | 1m |
| N246SF |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-06-06 16:10 UTC | 2026-06-06 16:22 UTC | 11m |
| N91AK |  | Naples Municipal Airport (KAPF) | Marco Island Executive Airport (KMKY) | 2026-06-06 15:28 UTC | 2026-06-06 16:15 UTC | 46m |
| N8314W |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-06-06 14:47 UTC | 2026-06-06 16:14 UTC | 1h 26m |
| N377DJ |  | Ocean County Airport (KMJX) | Ocean County Airport (KMJX) | 2026-06-06 16:07 UTC | 2026-06-06 16:13 UTC | 5m |
| OXF6154 | OXF | Falcon Field (KFFZ) | Nogales International Airport (KOLS) | 2026-06-06 14:54 UTC | 2026-06-06 16:12 UTC | 1h 17m |
| RVP953 | RVP | Cascais Airport (LPCS) | Portimão Airport (LPPM) | 2026-06-06 15:35 UTC | 2026-06-06 16:11 UTC | 35m |
| N475RC |  | Pleasant Valley Airstrip (24AZ) | Pleasant Valley Airstrip (24AZ) | 2026-06-06 15:58 UTC | 2026-06-06 16:09 UTC | 10m |
| N157CL |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-06 16:02 UTC | 2026-06-06 16:08 UTC | 6m |
| 504HW |  | Riego Flight Strip (38CL) | Riego Flight Strip (38CL) | 2026-06-06 15:41 UTC | 2026-06-06 16:07 UTC | 26m |
| FAC2351 | FAC | Madrid Air Base (SKMA) | Tunja Airport (SKTJ) | 2026-06-06 15:54 UTC | 2026-06-06 16:05 UTC | 11m |
| GTI8140 | GTI | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-06-06 11:42 UTC | 2026-06-06 16:05 UTC | 4h 22m |
| N8621E |  | Marv Skie-Lincoln County Airport (KY14) | Marv Skie-Lincoln County Airport (KY14) | 2026-06-06 15:48 UTC | 2026-06-06 16:05 UTC | 16m |
| ERU471 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-06-06 15:25 UTC | 2026-06-06 16:04 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
