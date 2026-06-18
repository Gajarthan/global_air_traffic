# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_13:56:33_UTC-green)

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

**Latest saved flight:** 2026-06-18 13:56:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-18 13:56:33 UTC

- **113,920** saved flights
- **39,534** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **113,920** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,387,485.5 tonnes** estimated CO2 emissions
- **80,433,942 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4696 |
| 2 | SkyWest Airlines | 4239 |
| 3 | EJA | 2205 |
| 4 | IndiGo | 2205 |
| 5 | American Airlines | 1795 |
| 6 | Southwest Airlines | 1692 |
| 7 | ENY | 1416 |
| 8 | Delta Air Lines | 1342 |
| 9 | Lufthansa | 1271 |
| 10 | Vueling | 1036 |
| 11 | WIF | 1013 |
| 12 | LATAM Airlines | 1008 |
| 13 | AZU | 955 |
| 14 | AXM | 948 |
| 15 | LXJ | 866 |
| 16 | Swiss International | 810 |
| 17 | All Nippon Airways | 788 |
| 18 | Alaska Airlines | 769 |
| 19 | QLK | 744 |
| 20 | easyJet | 731 |
| 21 | EJU | 716 |
| 22 | Cathay Pacific | 669 |
| 23 | AEE | 639 |
| 24 | VIV | 631 |
| 25 | Air France | 630 |
| 26 | United Airlines | 629 |
| 27 | CXK | 604 |
| 28 | MXY | 603 |
| 29 | AXB | 558 |
| 30 | GLO | 557 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95994 |
| 2 | 🇪🇸 ES | 7777 |
| 3 | 🇮🇳 IN | 6960 |
| 4 | 🇦🇺 AU | 6784 |
| 5 | 🇧🇷 BR | 6311 |
| 6 | 🇮🇹 IT | 6108 |
| 7 | 🇩🇪 DE | 6097 |
| 8 | 🇨🇦 CA | 5979 |
| 9 | 🇯🇵 JP | 5138 |
| 10 | 🇬🇧 GB | 4918 |
| 11 | 🇫🇷 FR | 4538 |
| 12 | 🇨🇴 CO | 3889 |
| 13 | 🇲🇽 MX | 3362 |
| 14 | 🇬🇷 GR | 3243 |
| 15 | 🇳🇴 NO | 3155 |
| 16 | 🇨🇭 CH | 2911 |
| 17 | 🇲🇾 MY | 2454 |
| 18 | 🇹🇷 TR | 2292 |
| 19 | 🇿🇦 ZA | 1931 |
| 20 | 🇳🇿 NZ | 1877 |
| 21 | 🇰🇷 KR | 1874 |
| 22 | 🇵🇱 PL | 1862 |
| 23 | 🇹🇭 TH | 1859 |
| 24 | 🇵🇭 PH | 1661 |
| 25 | 🇬🇹 GT | 1625 |
| 26 | 🇲🇦 MA | 1247 |
| 27 | 🇲🇴 MO | 1166 |
| 28 | 🇲🇪 ME | 1122 |
| 29 | 🇳🇱 NL | 1105 |
| 30 | 🇭🇷 HR | 992 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2419 |
| 2 | Denver International Airport |  | US | 1929 |
| 3 | Tokyo International Airport |  | JP | 1706 |
| 4 | Indira Gandhi International Airport |  | IN | 1518 |
| 5 | Guaymaral Airport |  | CO | 1441 |
| 6 | Harry Reid International Airport |  | US | 1429 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1402 |
| 8 | Zurich Airport |  | CH | 1278 |
| 9 | La Aurora Airport |  | GT | 1253 |
| 10 | Frankfurt am Main International Airport |  | DE | 1240 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1221 |
| 12 | Macau International Airport |  | MO | 1166 |
| 13 | El Dorado International Airport |  | CO | 1157 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1139 |
| 15 | Chicago O'Hare International Airport |  | US | 1124 |
| 16 | Capua Airport |  | IT | 989 |
| 17 | Madrid Barajas International Airport |  | ES | 981 |
| 18 | Salt Lake City International Airport |  | US | 966 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 957 |
| 20 | Kuala Lumpur International Airport |  | MY | 950 |
| 21 | Charlotte/Douglas International Airport |  | US | 882 |
| 22 | Congonhas Airport |  | BR | 874 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 852 |
| 24 | Charles de Gaulle International Airport |  | FR | 842 |
| 25 | Bengaluru International Airport |  | IN | 842 |
| 26 | Malpensa International Airport |  | IT | 818 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 809 |
| 28 | Ninoy Aquino International Airport |  | PH | 766 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 751 |
| 30 | Daniel K Inouye International Airport |  | US | 746 |
| 31 | Tenerife Norte Airport |  | ES | 741 |
| 32 | Barcelona International Airport |  | ES | 733 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 717 |
| 34 | Don Mueang International Airport |  | TH | 675 |
| 35 | Vitoria/Foronda Airport |  | ES | 674 |
| 36 | Amsterdam Airport Schiphol |  | NL | 674 |
| 37 | Calgary International Airport |  | CA | 670 |
| 38 | Seattle-Tacoma International Airport |  | US | 654 |
| 39 | Viracopos International Airport |  | BR | 654 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 650 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 598 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 412 | 21m | 244 km | 1,734.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 304 | 24m | 225 km | 1,179.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 297 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 280 | 1h 25m | 910 km | 4,393.9 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 278 | 14m | 114 km | 545.2 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 272 | 1h 10m | 770 km | 3,613.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 228 | 26m | 275 km | 1,080.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 212 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 167 | 22m | 55 km | 158.7 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 166 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 155 | 27m | 152 km | 405.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 151 | 44m | 452 km | 1,176.8 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 148 | 44m | 241 km | 614.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 145 | 20m | 250 km | 626.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 136 | 1h 1m | 695 km | 1,630.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 134 | 1h 43m | 1,423 km | 3,288.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 128 | 1h 17m | 961 km | 2,121.7 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 128 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 127 | 24m | 223 km | 488.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N381MG |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-06-18 13:35 UTC | 2026-06-18 13:56 UTC | 21m |
| N29BY |  | Brigham City Regional Airport (KBMC) | Scottsdale Airport (KSDL) | 2026-06-18 12:00 UTC | 2026-06-18 13:56 UTC | 1h 55m |
| OMA168 | Oman Air | Trabzon International Airport (LTCG) | Queen Alia International Airport (OJAI) | 2026-06-18 12:29 UTC | 2026-06-18 13:47 UTC | 1h 18m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-06-18 13:19 UTC | 2026-06-18 13:43 UTC | 24m |
| N9924W |  | Cecil Airport (KVQQ) | Reynolds Airpark (FL60) | 2026-06-18 13:01 UTC | 2026-06-18 13:39 UTC | 38m |
| UAE29V | Emirates | Dubai International Airport (OMDB) | Queen Alia International Airport (OJAI) | 2026-06-18 10:59 UTC | 2026-06-18 13:39 UTC | 2h 39m |
| ARCAS05 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-06-18 13:24 UTC | 2026-06-18 13:39 UTC | 14m |
| N738BJ |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-06-18 12:33 UTC | 2026-06-18 13:32 UTC | 59m |
| UAE175 | Emirates | Buhasa Airport (OMAB) | Queen Alia International Airport (OJAI) | 2026-06-18 10:39 UTC | 2026-06-18 13:32 UTC | 2h 52m |
| HK2078G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-18 12:53 UTC | 2026-06-18 13:32 UTC | 38m |
| XBGJV | XBG | Hermanos Serdan International Airport (MMPB) | Licenciado Benito Juarez International Airport (MMMX) | 2026-06-18 12:53 UTC | 2026-06-18 13:32 UTC | 38m |
| GFD10 | GFD | Schleswig Airport (ETNS) | Wunstorf Airport (ETNW) | 2026-06-18 11:36 UTC | 2026-06-18 13:27 UTC | 1h 51m |
| PAG4330 | PAG | Toronto Pearson International Airport (CYYZ) | South River/Sundridge Airport & Float Plane Base (CPE6) | 2026-06-18 12:53 UTC | 2026-06-18 13:25 UTC | 31m |
| N72EN |  | Scottsdale Airport (KSDL) | Glendale Regional Airport (KGEU) | 2026-06-18 13:14 UTC | 2026-06-18 13:24 UTC | 10m |
| SKW4338 | SkyWest Airlines | Detroit Metro Wayne County Airport (KDTW) | K8M8 (K8M8) | 2026-06-18 12:51 UTC | 2026-06-18 13:21 UTC | 29m |
| DERSW | DER | Donaueschingen-Villingen Airport (EDTD) | Friedrichshafen Airport (EDNY) | 2026-06-18 12:16 UTC | 2026-06-18 13:21 UTC | 1h 5m |
| HBZVU | HBZ | Samedan Airport (LSZS) | Reichenbach Air Base (LSGR) | 2026-06-18 12:44 UTC | 2026-06-18 13:21 UTC | 36m |
| DGAFC | DGA | Frankfurt-Egelsbach Airport (EDFE) | Mainz-Finthen Airport (EDFZ) | 2026-06-18 13:02 UTC | 2026-06-18 13:20 UTC | 18m |
| N570JA |  | Aurora Municipal Airport (KARR) | Lake In The Hills Airport (K3CK) | 2026-06-18 12:49 UTC | 2026-06-18 13:19 UTC | 30m |
| FMMCE | FMM | Montauban Airport (LFDB) | Clermont-Ferrand Auvergne Airport (LFLC) | 2026-06-18 12:19 UTC | 2026-06-18 13:19 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
