# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_15:06:10_UTC-green)

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

**Latest saved flight:** 2026-06-20 15:06:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-20 15:06:10 UTC

- **115,628** saved flights
- **40,068** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **115,628** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,406,463.7 tonnes** estimated CO2 emissions
- **81,534,127 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4770 |
| 2 | SkyWest Airlines | 4298 |
| 3 | EJA | 2240 |
| 4 | IndiGo | 2234 |
| 5 | American Airlines | 1808 |
| 6 | Southwest Airlines | 1718 |
| 7 | ENY | 1437 |
| 8 | Delta Air Lines | 1361 |
| 9 | Lufthansa | 1282 |
| 10 | Vueling | 1043 |
| 11 | WIF | 1024 |
| 12 | LATAM Airlines | 1018 |
| 13 | AZU | 965 |
| 14 | AXM | 953 |
| 15 | LXJ | 877 |
| 16 | Swiss International | 817 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 776 |
| 19 | QLK | 750 |
| 20 | easyJet | 742 |
| 21 | EJU | 728 |
| 22 | Cathay Pacific | 672 |
| 23 | AEE | 648 |
| 24 | United Airlines | 642 |
| 25 | VIV | 640 |
| 26 | Air France | 634 |
| 27 | CXK | 617 |
| 28 | MXY | 611 |
| 29 | AXB | 567 |
| 30 | GLO | 563 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 97635 |
| 2 | 🇪🇸 ES | 7880 |
| 3 | 🇮🇳 IN | 7041 |
| 4 | 🇦🇺 AU | 6858 |
| 5 | 🇧🇷 BR | 6373 |
| 6 | 🇮🇹 IT | 6194 |
| 7 | 🇩🇪 DE | 6168 |
| 8 | 🇨🇦 CA | 6077 |
| 9 | 🇯🇵 JP | 5185 |
| 10 | 🇬🇧 GB | 5022 |
| 11 | 🇫🇷 FR | 4592 |
| 12 | 🇨🇴 CO | 3980 |
| 13 | 🇲🇽 MX | 3407 |
| 14 | 🇬🇷 GR | 3297 |
| 15 | 🇳🇴 NO | 3186 |
| 16 | 🇨🇭 CH | 2953 |
| 17 | 🇲🇾 MY | 2470 |
| 18 | 🇹🇷 TR | 2340 |
| 19 | 🇿🇦 ZA | 1948 |
| 20 | 🇳🇿 NZ | 1899 |
| 21 | 🇵🇱 PL | 1894 |
| 22 | 🇰🇷 KR | 1882 |
| 23 | 🇹🇭 TH | 1881 |
| 24 | 🇵🇭 PH | 1682 |
| 25 | 🇬🇹 GT | 1637 |
| 26 | 🇲🇦 MA | 1257 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1140 |
| 29 | 🇳🇱 NL | 1118 |
| 30 | 🇭🇷 HR | 1004 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2443 |
| 2 | Denver International Airport |  | US | 1952 |
| 3 | Tokyo International Airport |  | JP | 1719 |
| 4 | Indira Gandhi International Airport |  | IN | 1541 |
| 5 | Guaymaral Airport |  | CO | 1473 |
| 6 | Harry Reid International Airport |  | US | 1448 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1418 |
| 8 | Zurich Airport |  | CH | 1289 |
| 9 | La Aurora Airport |  | GT | 1264 |
| 10 | Frankfurt am Main International Airport |  | DE | 1253 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1236 |
| 12 | El Dorado International Airport |  | CO | 1170 |
| 13 | Macau International Airport |  | MO | 1168 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1153 |
| 15 | Chicago O'Hare International Airport |  | US | 1136 |
| 16 | Capua Airport |  | IT | 1009 |
| 17 | Salt Lake City International Airport |  | US | 990 |
| 18 | Madrid Barajas International Airport |  | ES | 985 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 967 |
| 20 | Kuala Lumpur International Airport |  | MY | 954 |
| 21 | Charlotte/Douglas International Airport |  | US | 884 |
| 22 | Congonhas Airport |  | BR | 884 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 862 |
| 24 | Bengaluru International Airport |  | IN | 853 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 847 |
| 26 | Charles de Gaulle International Airport |  | FR | 846 |
| 27 | Malpensa International Airport |  | IT | 825 |
| 28 | Ninoy Aquino International Airport |  | PH | 776 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 758 |
| 30 | Daniel K Inouye International Airport |  | US | 752 |
| 31 | Tenerife Norte Airport |  | ES | 751 |
| 32 | Barcelona International Airport |  | ES | 738 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 729 |
| 34 | Don Mueang International Airport |  | TH | 682 |
| 35 | Vitoria/Foronda Airport |  | ES | 681 |
| 36 | Amsterdam Airport Schiphol |  | NL | 679 |
| 37 | Calgary International Airport |  | CA | 678 |
| 38 | Seattle-Tacoma International Airport |  | US | 665 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 660 |
| 40 | Viracopos International Airport |  | BR | 658 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 611 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 418 | 21m | 244 km | 1,760.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 309 | 24m | 225 km | 1,198.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 299 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 286 | 1h 7m | 706 km | 3,482.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 283 | 1h 25m | 910 km | 4,440.9 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 275 | 1h 10m | 770 km | 3,653.2 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 216 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 173 | 22m | 55 km | 164.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 152 | 44m | 241 km | 631.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 139 | 1h 44m | 1,423 km | 3,411.3 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 135 | 1h 39m | 1,156 km | 2,693.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 134 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 131 | 1h 17m | 961 km | 2,171.4 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N702GR |  | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-06-20 14:52 UTC | 2026-06-20 15:06 UTC | 13m |
| VAR493 | VAR | Phoenix Goodyear Airport (KGYR) | Buckeye Municipal Airport (KBXK) | 2026-06-20 14:29 UTC | 2026-06-20 15:00 UTC | 30m |
| EDV4750 | EDV | Hartsfield/Jackson Atlanta International Airport (KATL) | Yonder Airport (NC65) | 2026-06-20 14:12 UTC | 2026-06-20 14:59 UTC | 47m |
| N7995G |  | Malone Airport (NJ61) | Sky Manor Airport (KN40) | 2026-06-20 14:01 UTC | 2026-06-20 14:57 UTC | 55m |
| N70275 |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-06-20 14:46 UTC | 2026-06-20 14:56 UTC | 10m |
| TKF2 | TKF | Coventry Airport (EGBE) | Kemble Airport (EGBP) | 2026-06-20 14:31 UTC | 2026-06-20 14:56 UTC | 24m |
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-06-20 14:09 UTC | 2026-06-20 14:55 UTC | 45m |
| N268FM |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-06-20 13:58 UTC | 2026-06-20 14:54 UTC | 55m |
| N410FC |  | Chicago Executive Airport (KPWK) | Southern Wisconsin Regional Airport (KJVL) | 2026-06-20 13:54 UTC | 2026-06-20 14:52 UTC | 58m |
| N803JF |  | Newport Regional Airport (KM19) | Newport Regional Airport (KM19) | 2026-06-20 14:04 UTC | 2026-06-20 14:52 UTC | 48m |
| N492LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-20 13:59 UTC | 2026-06-20 14:50 UTC | 50m |
| N554R |  | Wood County Airport (K1G0) | Fulton County Airport (KUSE) | 2026-06-20 14:22 UTC | 2026-06-20 14:50 UTC | 27m |
| N20PN |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-06-20 14:22 UTC | 2026-06-20 14:44 UTC | 22m |
| SCA75 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-06-20 14:02 UTC | 2026-06-20 14:41 UTC | 39m |
| N713SQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-06-20 13:44 UTC | 2026-06-20 14:41 UTC | 57m |
| N10BB |  | Mid-Carolina Regional Airport (KRUQ) | Mid-Carolina Regional Airport (KRUQ) | 2026-06-20 14:24 UTC | 2026-06-20 14:38 UTC | 14m |
| XBPDM | XBP | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-06-20 14:08 UTC | 2026-06-20 14:38 UTC | 30m |
| AAL1597 | American Airlines | Laguardia Airport (KLGA) | Dallas-Fort Worth International Airport (KDFW) | 2026-06-20 11:26 UTC | 2026-06-20 14:37 UTC | 3h 11m |
| HBZVU | HBZ | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-06-20 14:20 UTC | 2026-06-20 14:35 UTC | 15m |
| SWR2LE | Swiss International | Gothenburg-Landvetter Airport (ESGG) | Zurich Airport (LSZH) | 2026-06-20 12:51 UTC | 2026-06-20 14:33 UTC | 1h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
