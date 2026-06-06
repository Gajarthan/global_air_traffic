# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_10:50:39_UTC-green)

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

**Latest saved flight:** 2026-06-06 10:50:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 10:50:39 UTC

- **103,598** saved flights
- **36,614** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **103,598** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,266,460.7 tonnes** estimated CO2 emissions
- **73,418,013 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4250 |
| 2 | SkyWest Airlines | 3898 |
| 3 | IndiGo | 2072 |
| 4 | EJA | 1983 |
| 5 | American Airlines | 1675 |
| 6 | Southwest Airlines | 1566 |
| 7 | ENY | 1289 |
| 8 | Delta Air Lines | 1226 |
| 9 | Lufthansa | 1194 |
| 10 | Vueling | 957 |
| 11 | LATAM Airlines | 916 |
| 12 | WIF | 911 |
| 13 | AXM | 894 |
| 14 | AZU | 830 |
| 15 | LXJ | 782 |
| 16 | Swiss International | 746 |
| 17 | All Nippon Airways | 731 |
| 18 | Alaska Airlines | 723 |
| 19 | QLK | 697 |
| 20 | easyJet | 670 |
| 21 | EJU | 648 |
| 22 | Cathay Pacific | 620 |
| 23 | AEE | 601 |
| 24 | VIV | 594 |
| 25 | Air France | 592 |
| 26 | United Airlines | 574 |
| 27 | MXY | 560 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 520 |
| 30 | AXB | 508 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87160 |
| 2 | 🇪🇸 ES | 7117 |
| 3 | 🇮🇳 IN | 6542 |
| 4 | 🇦🇺 AU | 6308 |
| 5 | 🇧🇷 BR | 5650 |
| 6 | 🇩🇪 DE | 5562 |
| 7 | 🇮🇹 IT | 5488 |
| 8 | 🇨🇦 CA | 5394 |
| 9 | 🇯🇵 JP | 4802 |
| 10 | 🇬🇧 GB | 4362 |
| 11 | 🇫🇷 FR | 4104 |
| 12 | 🇨🇴 CO | 3553 |
| 13 | 🇲🇽 MX | 3110 |
| 14 | 🇬🇷 GR | 2941 |
| 15 | 🇳🇴 NO | 2884 |
| 16 | 🇨🇭 CH | 2647 |
| 17 | 🇲🇾 MY | 2285 |
| 18 | 🇹🇷 TR | 1961 |
| 19 | 🇿🇦 ZA | 1798 |
| 20 | 🇳🇿 NZ | 1742 |
| 21 | 🇹🇭 TH | 1717 |
| 22 | 🇰🇷 KR | 1714 |
| 23 | 🇵🇱 PL | 1655 |
| 24 | 🇵🇭 PH | 1528 |
| 25 | 🇬🇹 GT | 1509 |
| 26 | 🇲🇦 MA | 1138 |
| 27 | 🇲🇴 MO | 1092 |
| 28 | 🇳🇱 NL | 1019 |
| 29 | 🇲🇪 ME | 976 |
| 30 | 🇭🇷 HR | 906 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2255 |
| 2 | Denver International Airport |  | US | 1776 |
| 3 | Tokyo International Airport |  | JP | 1594 |
| 4 | Indira Gandhi International Airport |  | IN | 1422 |
| 5 | Harry Reid International Airport |  | US | 1331 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1318 |
| 7 | Guaymaral Airport |  | CO | 1287 |
| 8 | Frankfurt am Main International Airport |  | DE | 1193 |
| 9 | Zurich Airport |  | CH | 1175 |
| 10 | La Aurora Airport |  | GT | 1162 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1120 |
| 12 | Macau International Airport |  | MO | 1092 |
| 13 | El Dorado International Airport |  | CO | 1088 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1051 |
| 15 | Chicago O'Hare International Airport |  | US | 1038 |
| 16 | Madrid Barajas International Airport |  | ES | 900 |
| 17 | Kuala Lumpur International Airport |  | MY | 895 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 888 |
| 19 | Salt Lake City International Airport |  | US | 878 |
| 20 | Capua Airport |  | IT | 861 |
| 21 | Charlotte/Douglas International Airport |  | US | 807 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 787 |
| 24 | Congonhas Airport |  | BR | 785 |
| 25 | Bengaluru International Airport |  | IN | 783 |
| 26 | Malpensa International Airport |  | IT | 779 |
| 27 | Daniel K Inouye International Airport |  | US | 712 |
| 28 | Tenerife Norte Airport |  | ES | 706 |
| 29 | Ninoy Aquino International Airport |  | PH | 697 |
| 30 | Barcelona International Airport |  | ES | 681 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 672 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 668 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 662 |
| 34 | Amsterdam Airport Schiphol |  | NL | 631 |
| 35 | Don Mueang International Airport |  | TH | 628 |
| 36 | Vitoria/Foronda Airport |  | ES | 622 |
| 37 | Calgary International Airport |  | CA | 616 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 600 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 590 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 531 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 380 | 21m | 244 km | 1,600.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 273 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 258 | 14m | 114 km | 506.0 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 255 | 1h 25m | 910 km | 4,001.5 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 239 | 1h 10m | 770 km | 3,174.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 134 | 18m | 144 km | 333.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 121 | 1h 43m | 1,423 km | 2,969.5 t |
| 28 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 52m | 1,304 km | 2,677.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| G72315 |  | El Paso International Airport (KELP) | El Paso International Airport (KELP) | 2026-06-06 10:39 UTC | 2026-06-06 10:50 UTC | 11m |
| HBKBT | HBK | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-06-06 09:57 UTC | 2026-06-06 10:43 UTC | 45m |
| REH98 | REH | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-06-06 09:42 UTC | 2026-06-06 10:35 UTC | 52m |
| CJT554 | CJT | Winnipeg James Armstrong Richardson International Airport (CYWG) | Montréal (Mirabel) Airport (CYMX) | 2026-06-06 08:10 UTC | 2026-06-06 10:33 UTC | 2h 23m |
| APZ112 | APZ | San Francisco International Airport (KSFO) | Incheon International Airport (RKSI) | 2026-06-05 22:45 UTC | 2026-06-06 10:27 UTC | 11h 42m |
| DEOJE | DEO | Giebelstadt Airport (EDQG) | Koblenz-Winningen Airport (EDRK) | 2026-06-06 08:45 UTC | 2026-06-06 10:27 UTC | 1h 42m |
| DELTX | DEL | Neumunster Airport (EDHN) | Neumunster Airport (EDHN) | 2026-06-06 10:16 UTC | 2026-06-06 10:27 UTC | 10m |
| HLC276 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-06-06 10:06 UTC | 2026-06-06 10:27 UTC | 20m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-06 10:07 UTC | 2026-06-06 10:20 UTC | 13m |
| FHSKJ | FHS | Paris-Le Bourget Airport (LFPB) | L'alpe D'huez Airport (LFHU) | 2026-06-06 08:37 UTC | 2026-06-06 10:17 UTC | 1h 40m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-06-06 09:07 UTC | 2026-06-06 10:15 UTC | 1h 8m |
| IGO7126 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Mysore Airport (VOMY) | 2026-06-06 05:03 UTC | 2026-06-06 10:06 UTC | 5h 3m |
| RUK7547 | RUK | Poznań-Ławica Airport (EPPO) | Wickenby Aerodrome (EGNW) | 2026-06-06 08:07 UTC | 2026-06-06 10:00 UTC | 1h 53m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-06-06 09:46 UTC | 2026-06-06 09:57 UTC | 11m |
| RYR5368 | Ryanair | Castellon-Costa Azahar Airport (LEDS) | Monchengladbach Airport (EDLN) | 2026-06-06 08:03 UTC | 2026-06-06 09:56 UTC | 1h 52m |
| TUI21W | TUI | Son Bonet Airport (LESB) | Norvenich Airport (ETNN) | 2026-06-06 08:03 UTC | 2026-06-06 09:56 UTC | 1h 52m |
| RYR35CB | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Visoko Sport Airfield (LQVI) | 2026-06-06 08:45 UTC | 2026-06-06 09:55 UTC | 1h 9m |
| WIF153 | WIF | Sogndal Airport (ENSG) | Sogndal Airport (ENSG) | 2026-06-06 09:40 UTC | 2026-06-06 09:55 UTC | 15m |
| UPS706 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Winona-Montgomery County Airport (K5A6) | 2026-06-06 09:04 UTC | 2026-06-06 09:52 UTC | 48m |
| DLH3HX | Lufthansa | Munich International Airport (EDDM) | Cluj-Napoca International Airport (LRCL) | 2026-06-06 08:44 UTC | 2026-06-06 09:50 UTC | 1h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
