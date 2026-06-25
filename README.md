# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_10:37:40_UTC-green)

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

**Latest saved flight:** 2026-06-25 10:37:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-25 10:37:40 UTC

- **119,810** saved flights
- **41,237** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **119,810** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,449,547.1 tonnes** estimated CO2 emissions
- **84,031,716 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4928 |
| 2 | SkyWest Airlines | 4418 |
| 3 | EJA | 2313 |
| 4 | IndiGo | 2307 |
| 5 | American Airlines | 1861 |
| 6 | Southwest Airlines | 1785 |
| 7 | ENY | 1493 |
| 8 | Delta Air Lines | 1417 |
| 9 | Lufthansa | 1314 |
| 10 | Vueling | 1077 |
| 11 | WIF | 1063 |
| 12 | LATAM Airlines | 1060 |
| 13 | AZU | 997 |
| 14 | AXM | 978 |
| 15 | LXJ | 909 |
| 16 | Swiss International | 842 |
| 17 | All Nippon Airways | 820 |
| 18 | Alaska Airlines | 792 |
| 19 | easyJet | 771 |
| 20 | QLK | 768 |
| 21 | EJU | 750 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 667 |
| 24 | United Airlines | 656 |
| 25 | VIV | 656 |
| 26 | Air France | 654 |
| 27 | CXK | 639 |
| 28 | MXY | 630 |
| 29 | AXB | 596 |
| 30 | JetBlue | 593 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 101396 |
| 2 | 🇪🇸 ES | 8146 |
| 3 | 🇮🇳 IN | 7250 |
| 4 | 🇦🇺 AU | 7068 |
| 5 | 🇧🇷 BR | 6590 |
| 6 | 🇩🇪 DE | 6410 |
| 7 | 🇮🇹 IT | 6392 |
| 8 | 🇨🇦 CA | 6300 |
| 9 | 🇯🇵 JP | 5350 |
| 10 | 🇬🇧 GB | 5263 |
| 11 | 🇫🇷 FR | 4774 |
| 12 | 🇨🇴 CO | 4012 |
| 13 | 🇲🇽 MX | 3495 |
| 14 | 🇬🇷 GR | 3415 |
| 15 | 🇳🇴 NO | 3298 |
| 16 | 🇨🇭 CH | 3082 |
| 17 | 🇲🇾 MY | 2539 |
| 18 | 🇹🇷 TR | 2465 |
| 19 | 🇿🇦 ZA | 2021 |
| 20 | 🇵🇱 PL | 1969 |
| 21 | 🇳🇿 NZ | 1942 |
| 22 | 🇹🇭 TH | 1916 |
| 23 | 🇰🇷 KR | 1904 |
| 24 | 🇵🇭 PH | 1721 |
| 25 | 🇬🇹 GT | 1675 |
| 26 | 🇲🇦 MA | 1293 |
| 27 | 🇲🇪 ME | 1197 |
| 28 | 🇲🇴 MO | 1173 |
| 29 | 🇳🇱 NL | 1149 |
| 30 | 🇭🇷 HR | 1037 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2517 |
| 2 | Denver International Airport |  | US | 2009 |
| 3 | Tokyo International Airport |  | JP | 1771 |
| 4 | Indira Gandhi International Airport |  | IN | 1595 |
| 5 | Guaymaral Airport |  | CO | 1502 |
| 6 | Harry Reid International Airport |  | US | 1490 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1453 |
| 8 | Zurich Airport |  | CH | 1336 |
| 9 | La Aurora Airport |  | GT | 1293 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1272 |
| 11 | Frankfurt am Main International Airport |  | DE | 1268 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1184 |
| 13 | Macau International Airport |  | MO | 1173 |
| 14 | El Dorado International Airport |  | CO | 1171 |
| 15 | Chicago O'Hare International Airport |  | US | 1170 |
| 16 | Capua Airport |  | IT | 1031 |
| 17 | Salt Lake City International Airport |  | US | 1030 |
| 18 | Madrid Barajas International Airport |  | ES | 1009 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1000 |
| 20 | Kuala Lumpur International Airport |  | MY | 982 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 925 |
| 22 | Congonhas Airport |  | BR | 921 |
| 23 | Charlotte/Douglas International Airport |  | US | 908 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 890 |
| 25 | Charles de Gaulle International Airport |  | FR | 877 |
| 26 | Bengaluru International Airport |  | IN | 874 |
| 27 | Malpensa International Airport |  | IT | 838 |
| 28 | Ninoy Aquino International Airport |  | PH | 797 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 782 |
| 30 | Daniel K Inouye International Airport |  | US | 772 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 757 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 735 |
| 34 | Calgary International Airport |  | CA | 700 |
| 35 | Vitoria/Foronda Airport |  | ES | 699 |
| 36 | Amsterdam Airport Schiphol |  | NL | 695 |
| 37 | Don Mueang International Airport |  | TH | 694 |
| 38 | Seattle-Tacoma International Airport |  | US | 688 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 680 |
| 40 | Scottsdale Airport |  | US | 679 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 625 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 434 | 21m | 244 km | 1,827.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 315 | 24m | 225 km | 1,222.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 307 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 291 | 1h 25m | 910 km | 4,566.5 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 289 | 1h 10m | 770 km | 3,839.1 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 236 | 26m | 275 km | 1,118.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 223 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 177 | 22m | 55 km | 168.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 172 | 27m | 215 km | 637.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 164 | 44m | 241 km | 681.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 150 | 1h 44m | 1,423 km | 3,681.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 149 | 18m | 144 km | 370.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 141 | 1h 38m | 1,156 km | 2,812.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 135 | 1h 17m | 961 km | 2,237.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HTY206 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-06-25 10:10 UTC | 2026-06-25 10:37 UTC | 27m |
| ZAM26 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-25 09:57 UTC | 2026-06-25 10:35 UTC | 37m |
| ZAM15 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-25 09:56 UTC | 2026-06-25 10:31 UTC | 35m |
| FSMU1P | FSM | Son Bonet Airport (LESB) | Reus Air Base (LERS) | 2026-06-25 09:18 UTC | 2026-06-25 10:27 UTC | 1h 8m |
| MSEXY | MSE | Eleftherios Venizelos International Airport (LGAV) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-25 07:12 UTC | 2026-06-25 10:05 UTC | 2h 52m |
| AYT105 | AYT | Hatzor Air Base (LLHS) | Ein Yahav Airfield (LLEY) | 2026-06-25 09:45 UTC | 2026-06-25 10:01 UTC | 15m |
| YGI | YGI | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-06-25 09:14 UTC | 2026-06-25 10:01 UTC | 47m |
| DEAPR | DEA | Lubeck Blankensee Airport (EDHL) | Lubeck Blankensee Airport (EDHL) | 2026-06-25 10:00 UTC | 2026-06-25 10:00 UTC | 0m |
| GRZL41 | GRZ | Pardubice Airport (LKPD) | Pardubice Airport (LKPD) | 2026-06-25 09:00 UTC | 2026-06-25 09:57 UTC | 57m |
| JBU767 | JetBlue | Orlando International Airport (KMCO) | North Eleuthera Airport (MYEH) | 2026-06-25 09:12 UTC | 2026-06-25 09:56 UTC | 44m |
| QR9950 |  | Doha International Airport (OTBD) | Doha International Airport (OTBD) | 2026-06-25 08:56 UTC | 2026-06-25 09:55 UTC | 59m |
| EJU926U | EJU | Malpensa International Airport (LIMC) | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | 2026-06-25 09:02 UTC | 2026-06-25 09:54 UTC | 52m |
| YLEVI | YLE | Adazi Airfield (EVAD) | Adazi Airfield (EVAD) | 2026-06-25 09:51 UTC | 2026-06-25 09:51 UTC | 0m |
| DSO23MJ | DSO | Hartsfield/Jackson Atlanta International Airport (KATL) | Bassatine Airport (GMFM) | 2026-06-25 02:30 UTC | 2026-06-25 09:50 UTC | 7h 19m |
| VOE6AJ | VOE | Strasbourg Airport (LFST) | Calvi-Sainte-Catherine Airport (LFKC) | 2026-06-25 08:21 UTC | 2026-06-25 09:48 UTC | 1h 27m |
| UPS1468 | UPS | Louisville Muhammad Ali International Airport (KSDF) | II20 (II20) | 2026-06-25 09:19 UTC | 2026-06-25 09:46 UTC | 26m |
| 4XDAN |  | Bar Yehuda Airfield (LLMZ) | Bar Yehuda Airfield (LLMZ) | 2026-06-25 09:38 UTC | 2026-06-25 09:45 UTC | 6m |
| GAF199 | GAF | Celle Airport (ETHC) | Celle Airport (ETHC) | 2026-06-25 08:16 UTC | 2026-06-25 09:45 UTC | 1h 28m |
| FJO53F | FJO | Jersey Airport (EGJJ) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-25 08:13 UTC | 2026-06-25 09:44 UTC | 1h 30m |
| SWR2TM | Swiss International | Malpensa International Airport (LIMC) | Zurich Airport (LSZH) | 2026-06-25 09:00 UTC | 2026-06-25 09:36 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
