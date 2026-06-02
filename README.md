# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_10:42:31_UTC-green)

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

**Latest saved flight:** 2026-06-02 10:42:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-02 10:42:31 UTC

- **100,799** saved flights
- **35,765** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **100,799** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,234,082.3 tonnes** estimated CO2 emissions
- **71,541,002 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4167 |
| 2 | SkyWest Airlines | 3790 |
| 3 | IndiGo | 2030 |
| 4 | EJA | 1922 |
| 5 | American Airlines | 1631 |
| 6 | Southwest Airlines | 1529 |
| 7 | ENY | 1257 |
| 8 | Delta Air Lines | 1186 |
| 9 | Lufthansa | 1179 |
| 10 | Vueling | 941 |
| 11 | LATAM Airlines | 897 |
| 12 | WIF | 883 |
| 13 | AXM | 871 |
| 14 | AZU | 811 |
| 15 | LXJ | 761 |
| 16 | Swiss International | 736 |
| 17 | All Nippon Airways | 717 |
| 18 | Alaska Airlines | 704 |
| 19 | QLK | 678 |
| 20 | easyJet | 655 |
| 21 | EJU | 634 |
| 22 | Cathay Pacific | 605 |
| 23 | AEE | 589 |
| 24 | Air France | 584 |
| 25 | VIV | 581 |
| 26 | United Airlines | 565 |
| 27 | CXK | 542 |
| 28 | MXY | 539 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 498 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 84453 |
| 2 | 🇪🇸 ES | 6980 |
| 3 | 🇮🇳 IN | 6418 |
| 4 | 🇦🇺 AU | 6105 |
| 5 | 🇧🇷 BR | 5506 |
| 6 | 🇩🇪 DE | 5455 |
| 7 | 🇮🇹 IT | 5376 |
| 8 | 🇨🇦 CA | 5200 |
| 9 | 🇯🇵 JP | 4687 |
| 10 | 🇬🇧 GB | 4285 |
| 11 | 🇫🇷 FR | 4026 |
| 12 | 🇨🇴 CO | 3495 |
| 13 | 🇲🇽 MX | 3048 |
| 14 | 🇬🇷 GR | 2875 |
| 15 | 🇳🇴 NO | 2795 |
| 16 | 🇨🇭 CH | 2603 |
| 17 | 🇲🇾 MY | 2218 |
| 18 | 🇹🇷 TR | 1912 |
| 19 | 🇿🇦 ZA | 1763 |
| 20 | 🇳🇿 NZ | 1693 |
| 21 | 🇹🇭 TH | 1679 |
| 22 | 🇰🇷 KR | 1639 |
| 23 | 🇵🇱 PL | 1618 |
| 24 | 🇬🇹 GT | 1491 |
| 25 | 🇵🇭 PH | 1471 |
| 26 | 🇲🇦 MA | 1130 |
| 27 | 🇲🇴 MO | 1066 |
| 28 | 🇳🇱 NL | 1005 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 890 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2199 |
| 2 | Denver International Airport |  | US | 1731 |
| 3 | Tokyo International Airport |  | JP | 1556 |
| 4 | Indira Gandhi International Airport |  | IN | 1394 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1295 |
| 6 | Harry Reid International Airport |  | US | 1288 |
| 7 | Guaymaral Airport |  | CO | 1262 |
| 8 | Frankfurt am Main International Airport |  | DE | 1182 |
| 9 | Zurich Airport |  | CH | 1155 |
| 10 | La Aurora Airport |  | GT | 1146 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1092 |
| 12 | El Dorado International Airport |  | CO | 1074 |
| 13 | Macau International Airport |  | MO | 1066 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1022 |
| 15 | Chicago O'Hare International Airport |  | US | 1012 |
| 16 | Kuala Lumpur International Airport |  | MY | 878 |
| 17 | Madrid Barajas International Airport |  | ES | 877 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 867 |
| 19 | Salt Lake City International Airport |  | US | 854 |
| 20 | Capua Airport |  | IT | 835 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 784 |
| 22 | Charlotte/Douglas International Airport |  | US | 784 |
| 23 | Charles de Gaulle International Airport |  | FR | 775 |
| 24 | Malpensa International Airport |  | IT | 768 |
| 25 | Bengaluru International Airport |  | IN | 768 |
| 26 | Congonhas Airport |  | BR | 766 |
| 27 | Daniel K Inouye International Airport |  | US | 697 |
| 28 | Tenerife Norte Airport |  | ES | 696 |
| 29 | Ninoy Aquino International Airport |  | PH | 672 |
| 30 | Barcelona International Airport |  | ES | 666 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 658 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 656 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 643 |
| 34 | Amsterdam Airport Schiphol |  | NL | 621 |
| 35 | Don Mueang International Airport |  | TH | 616 |
| 36 | Vitoria/Foronda Airport |  | ES | 612 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 590 |
| 39 | Seattle-Tacoma International Airport |  | US | 580 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 520 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 366 | 21m | 244 km | 1,541.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 269 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 265 | 24m | 225 km | 1,028.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 248 | 1h 26m | 910 km | 3,891.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 244 | 28m | 304 km | 1,279.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 211 | 19m | 165 km | 600.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 198 | 26m | 275 km | 938.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 157 | 20m | 99 km | 268.9 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 146 | 14m | 154 km | 386.8 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 146 | 22m | 55 km | 138.8 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 141 | 31m | 369 km | 897.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 133 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 127 | 1h 39m | 1,156 km | 2,533.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 126 | 1h 1m | 695 km | 1,510.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N917JB |  | MI95 (MI95) | Dowagiac Municipal Airport (KC91) | 2026-06-02 10:31 UTC | 2026-06-02 10:42 UTC | 10m |
| ZKIDU | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-06-02 10:22 UTC | 2026-06-02 10:40 UTC | 17m |
| N257EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-06-02 07:50 UTC | 2026-06-02 10:37 UTC | 2h 46m |
| LTA903 | LTA | Indianapolis International Airport (KIND) | Skeeter Landing Airport (II97) | 2026-06-02 10:19 UTC | 2026-06-02 10:34 UTC | 14m |
| RYR380A | Ryanair | Palma De Mallorca Airport (LEPA) | Ansbach-Petersdorf Airport (EDQF) | 2026-06-02 08:22 UTC | 2026-06-02 10:11 UTC | 1h 49m |
| SAS2026 | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Ornskoldsvik Airport (ESNO) | 2026-06-02 09:26 UTC | 2026-06-02 10:06 UTC | 40m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Kauhajoki Airport (EFKJ) | 2026-06-02 09:21 UTC | 2026-06-02 10:04 UTC | 43m |
| RYR484A | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | L'Aquila / Preturo Airport (LIAP) | 2026-06-02 09:16 UTC | 2026-06-02 10:04 UTC | 47m |
| WMT4LW | WMT | Paris Beauvais Tille Airport (LFOB) | Iasi Airport (LRIA) | 2026-06-02 07:43 UTC | 2026-06-02 10:03 UTC | 2h 20m |
| HBXCL | HBX | Courchevel Airport (LFLJ) | Muenster Aero Airport (LSPU) | 2026-06-02 09:40 UTC | 2026-06-02 10:03 UTC | 22m |
| SFJ15 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-06-02 08:56 UTC | 2026-06-02 10:03 UTC | 1h 6m |
| AIQ3207 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-06-02 09:11 UTC | 2026-06-02 10:01 UTC | 50m |
| AIQ3231 | AIQ | Don Mueang International Airport (VTBD) | Chumphon Airport (VTSE) | 2026-06-02 09:26 UTC | 2026-06-02 10:00 UTC | 34m |
| IGO6485 | IndiGo | Gaya Airport (VEGY) | Sarsawa Air Force Station (VISP) | 2026-06-02 08:44 UTC | 2026-06-02 10:00 UTC | 1h 15m |
| AYAL | AYA | Nevatim Air Base (LLNV) | Ein Yahav Airfield (LLEY) | 2026-06-02 09:45 UTC | 2026-06-02 09:59 UTC | 13m |
| AFR32GL | Air France | Charles de Gaulle International Airport (LFPG) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-06-02 08:11 UTC | 2026-06-02 09:59 UTC | 1h 47m |
| SWR2DV | Swiss International | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 2026-06-02 08:50 UTC | 2026-06-02 09:55 UTC | 1h 4m |
| CTV992 | CTV | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-06-02 09:38 UTC | 2026-06-02 09:55 UTC | 16m |
| RYR1HU | Ryanair | Vienna International Airport (LOWW) | Corte Airport (LFKT) | 2026-06-02 08:41 UTC | 2026-06-02 09:53 UTC | 1h 12m |
| SWR2TM | Swiss International | Malpensa International Airport (LIMC) | Zurich Airport (LSZH) | 2026-06-02 09:19 UTC | 2026-06-02 09:52 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
