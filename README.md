# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_06:47:00_UTC-green)

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

**Latest saved flight:** 2026-06-03 06:47:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-03 06:47:00 UTC

- **101,451** saved flights
- **35,958** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **101,451** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,241,796.0 tonnes** estimated CO2 emissions
- **71,988,172 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4191 |
| 2 | SkyWest Airlines | 3808 |
| 3 | IndiGo | 2038 |
| 4 | EJA | 1931 |
| 5 | American Airlines | 1637 |
| 6 | Southwest Airlines | 1537 |
| 7 | ENY | 1259 |
| 8 | Delta Air Lines | 1191 |
| 9 | Lufthansa | 1186 |
| 10 | Vueling | 947 |
| 11 | LATAM Airlines | 900 |
| 12 | WIF | 889 |
| 13 | AXM | 878 |
| 14 | AZU | 818 |
| 15 | LXJ | 762 |
| 16 | Swiss International | 737 |
| 17 | All Nippon Airways | 718 |
| 18 | Alaska Airlines | 712 |
| 19 | QLK | 682 |
| 20 | easyJet | 658 |
| 21 | EJU | 637 |
| 22 | Cathay Pacific | 615 |
| 23 | AEE | 589 |
| 24 | Air France | 586 |
| 25 | VIV | 586 |
| 26 | United Airlines | 566 |
| 27 | CXK | 545 |
| 28 | MXY | 544 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 500 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 85067 |
| 2 | 🇪🇸 ES | 7014 |
| 3 | 🇮🇳 IN | 6448 |
| 4 | 🇦🇺 AU | 6161 |
| 5 | 🇧🇷 BR | 5539 |
| 6 | 🇩🇪 DE | 5481 |
| 7 | 🇮🇹 IT | 5405 |
| 8 | 🇨🇦 CA | 5257 |
| 9 | 🇯🇵 JP | 4699 |
| 10 | 🇬🇧 GB | 4301 |
| 11 | 🇫🇷 FR | 4046 |
| 12 | 🇨🇴 CO | 3505 |
| 13 | 🇲🇽 MX | 3069 |
| 14 | 🇬🇷 GR | 2887 |
| 15 | 🇳🇴 NO | 2815 |
| 16 | 🇨🇭 CH | 2613 |
| 17 | 🇲🇾 MY | 2240 |
| 18 | 🇹🇷 TR | 1925 |
| 19 | 🇿🇦 ZA | 1769 |
| 20 | 🇳🇿 NZ | 1709 |
| 21 | 🇹🇭 TH | 1690 |
| 22 | 🇰🇷 KR | 1645 |
| 23 | 🇵🇱 PL | 1627 |
| 24 | 🇬🇹 GT | 1501 |
| 25 | 🇵🇭 PH | 1485 |
| 26 | 🇲🇦 MA | 1132 |
| 27 | 🇲🇴 MO | 1074 |
| 28 | 🇳🇱 NL | 1009 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 897 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2206 |
| 2 | Denver International Airport |  | US | 1739 |
| 3 | Tokyo International Airport |  | JP | 1557 |
| 4 | Indira Gandhi International Airport |  | IN | 1402 |
| 5 | Harry Reid International Airport |  | US | 1300 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1299 |
| 7 | Guaymaral Airport |  | CO | 1267 |
| 8 | Frankfurt am Main International Airport |  | DE | 1186 |
| 9 | Zurich Airport |  | CH | 1163 |
| 10 | La Aurora Airport |  | GT | 1154 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1096 |
| 12 | El Dorado International Airport |  | CO | 1075 |
| 13 | Macau International Airport |  | MO | 1074 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1027 |
| 15 | Chicago O'Hare International Airport |  | US | 1014 |
| 16 | Kuala Lumpur International Airport |  | MY | 885 |
| 17 | Madrid Barajas International Airport |  | ES | 883 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 872 |
| 19 | Salt Lake City International Airport |  | US | 855 |
| 20 | Capua Airport |  | IT | 841 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 792 |
| 22 | Charlotte/Douglas International Airport |  | US | 787 |
| 23 | Charles de Gaulle International Airport |  | FR | 780 |
| 24 | Malpensa International Airport |  | IT | 771 |
| 25 | Bengaluru International Airport |  | IN | 770 |
| 26 | Congonhas Airport |  | BR | 769 |
| 27 | Daniel K Inouye International Airport |  | US | 703 |
| 28 | Tenerife Norte Airport |  | ES | 698 |
| 29 | Ninoy Aquino International Airport |  | PH | 679 |
| 30 | Barcelona International Airport |  | ES | 671 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 661 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 659 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 647 |
| 34 | Amsterdam Airport Schiphol |  | NL | 623 |
| 35 | Don Mueang International Airport |  | TH | 618 |
| 36 | Vitoria/Foronda Airport |  | ES | 615 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 596 |
| 39 | Seattle-Tacoma International Airport |  | US | 585 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 575 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 522 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 372 | 21m | 244 km | 1,566.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 271 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 268 | 24m | 225 km | 1,039.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 249 | 1h 26m | 910 km | 3,907.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 246 | 28m | 304 km | 1,289.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 214 | 19m | 165 km | 608.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 200 | 26m | 275 km | 947.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 149 | 22m | 55 km | 141.6 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 142 | 31m | 369 km | 903.9 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 135 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 131 | 20m | 147 km | 331.5 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VLG4UD | Vueling | Sevilla Airport (LEZL) | Tenerife Norte Airport (GCXO) | 2026-06-03 04:41 UTC | 2026-06-03 06:47 UTC | 2h 5m |
| T8A212 |  | Palau International Airport (PTRO) | Palau International Airport (PTRO) | 2026-06-03 06:29 UTC | 2026-06-03 06:44 UTC | 14m |
| CFG5JK | CFG | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-06-03 06:12 UTC | 2026-06-03 06:42 UTC | 29m |
| AFL904 | AFL | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-06-03 05:31 UTC | 2026-06-03 06:33 UTC | 1h 2m |
| TSW1M | TSW | Linate Airport (LIML) | Raron Airport (LSTA) | 2026-06-03 06:02 UTC | 2026-06-03 06:29 UTC | 26m |
| NV123 |  | Sydney Bankstown Airport (YSBK) | Orange Airport (YORG) | 2026-06-03 06:01 UTC | 2026-06-03 06:28 UTC | 26m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-06-03 05:02 UTC | 2026-06-03 06:23 UTC | 1h 21m |
| 4LGCG |  | UG27 (UG27) | UG27 (UG27) | 2026-06-03 06:14 UTC | 2026-06-03 06:22 UTC | 8m |
| JYRJK | JYR | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-06-03 06:00 UTC | 2026-06-03 06:17 UTC | 17m |
| RYR1WP | Ryanair | Berlin Brandenburg Airport (EDDB) | Sofia Airport (LBSF) | 2026-06-03 04:25 UTC | 2026-06-03 06:14 UTC | 1h 49m |
| EWG4Z | EWG | Berlin Brandenburg Airport (EDDB) | Zurich Airport (LSZH) | 2026-06-03 05:01 UTC | 2026-06-03 06:13 UTC | 1h 12m |
| VPBIB | VPB | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-06-03 06:02 UTC | 2026-06-03 06:13 UTC | 10m |
| BLINR47 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-06-03 05:47 UTC | 2026-06-03 06:10 UTC | 22m |
| ASA1112 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-06-03 05:47 UTC | 2026-06-03 06:08 UTC | 21m |
| N486LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-03 05:07 UTC | 2026-06-03 06:07 UTC | 1h 0m |
| RYR8070 | Ryanair | Marseille Provence Airport (LFML) | Gunzenhausen-Reutberg Airport (EDMH) | 2026-06-03 04:50 UTC | 2026-06-03 06:06 UTC | 1h 15m |
| WIF451 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-06-03 05:39 UTC | 2026-06-03 06:04 UTC | 24m |
| CJT626 | CJT | Montréal (Mirabel) Airport (CYMX) | Chipman Airport (CCS4) | 2026-06-03 05:09 UTC | 2026-06-03 06:01 UTC | 52m |
| THA132 | Thai Airways | Suvarnabhumi Airport (VTBS) | Kengtung Airport (VYKG) | 2026-06-03 05:06 UTC | 2026-06-03 05:59 UTC | 53m |
| N801XA |  | King Fahd International Airport (OEDF) | Al Ahsa Airport (OEAH) | 2026-06-03 05:47 UTC | 2026-06-03 05:59 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
