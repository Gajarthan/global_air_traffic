# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_11:41:31_UTC-green)

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

**Latest saved flight:** 2026-08-07 11:41:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 11:41:31 UTC

- **175,136** saved flights
- **56,570** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **175,136** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,108,343.8 tonnes** estimated CO2 emissions
- **122,222,826 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6948 |
| 2 | SkyWest Airlines | 6391 |
| 3 | EJA | 3458 |
| 4 | IndiGo | 3076 |
| 5 | Southwest Airlines | 2755 |
| 6 | American Airlines | 2735 |
| 7 | ENY | 2173 |
| 8 | Delta Air Lines | 2069 |
| 9 | LATAM Airlines | 1617 |
| 10 | Lufthansa | 1581 |
| 11 | AZU | 1548 |
| 12 | WIF | 1468 |
| 13 | Vueling | 1441 |
| 14 | LXJ | 1370 |
| 15 | AXM | 1195 |
| 16 | Swiss International | 1193 |
| 17 | easyJet | 1192 |
| 18 | QLK | 1082 |
| 19 | EJU | 1071 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1065 |
| 22 | VIV | 963 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 927 |
| 25 | GLO | 921 |
| 26 | AEE | 915 |
| 27 | United Airlines | 907 |
| 28 | Air France | 902 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150444 |
| 2 | 🇪🇸 ES | 11210 |
| 3 | 🇧🇷 BR | 9955 |
| 4 | 🇦🇺 AU | 9948 |
| 5 | 🇮🇳 IN | 9639 |
| 6 | 🇨🇦 CA | 9566 |
| 7 | 🇮🇹 IT | 9047 |
| 8 | 🇩🇪 DE | 8686 |
| 9 | 🇬🇧 GB | 8118 |
| 10 | 🇯🇵 JP | 7073 |
| 11 | 🇫🇷 FR | 6959 |
| 12 | 🇨🇴 CO | 6423 |
| 13 | 🇬🇷 GR | 5099 |
| 14 | 🇲🇽 MX | 5005 |
| 15 | 🇨🇭 CH | 4640 |
| 16 | 🇳🇴 NO | 4563 |
| 17 | 🇹🇷 TR | 4321 |
| 18 | 🇲🇾 MY | 3118 |
| 19 | 🇵🇱 PL | 2925 |
| 20 | 🇿🇦 ZA | 2848 |
| 21 | 🇹🇭 TH | 2600 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2324 |
| 24 | 🇬🇹 GT | 2227 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1765 |
| 27 | 🇭🇷 HR | 1709 |
| 28 | 🇲🇪 ME | 1603 |
| 29 | 🇳🇱 NL | 1579 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3606 |
| 2 | Denver International Airport |  | US | 2891 |
| 3 | Tokyo International Airport |  | JP | 2207 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2140 |
| 6 | Harry Reid International Airport |  | US | 2089 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1902 |
| 8 | Zurich Airport |  | CH | 1856 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1829 |
| 10 | La Aurora Airport |  | GT | 1714 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1543 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1440 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1422 |
| 19 | Capua Airport |  | IT | 1368 |
| 20 | Madrid Barajas International Airport |  | ES | 1364 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1232 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1191 |
| 26 | Charles de Gaulle International Airport |  | FR | 1191 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1145 |
| 29 | Ninoy Aquino International Airport |  | PH | 1093 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1084 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1080 |
| 32 | Barcelona International Airport |  | ES | 1036 |
| 33 | Daniel K Inouye International Airport |  | US | 1009 |
| 34 | Seattle-Tacoma International Airport |  | US | 1008 |
| 35 | Viracopos International Airport |  | BR | 992 |
| 36 | Calgary International Airport |  | CA | 992 |
| 37 | Reno/Tahoe International Airport |  | US | 991 |
| 38 | Oslo Gardermoen Airport |  | NO | 976 |
| 39 | Tenerife Norte Airport |  | ES | 966 |
| 40 | Amsterdam Airport Schiphol |  | NL | 950 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 640 | 21m | 244 km | 2,694.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 405 | 1h 8m | 770 km | 5,380.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 322 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 264 | 44m | 241 km | 1,096.6 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 240 | 1h 48m | 1,423 km | 5,890.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 230 | 20m | 250 km | 993.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 224 | 26m | 215 km | 829.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 215 | 20m | 99 km | 368.3 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 208 | 19m | 144 km | 517.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 24 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 206 | 8m | - | - |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 198 | 24m | 218 km | 745.9 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 191 | 43m | 452 km | 1,488.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IMIAW | IMI | Megeve Airport (LFHM) | Aosta Airport (LIMW) | 2026-08-07 10:55 UTC | 2026-08-07 11:41 UTC | 46m |
| ABX552 | ABX | Cincinnati/Northern Kentucky International Airport (KCVG) | John F Kennedy International Airport (KJFK) | 2026-08-07 09:54 UTC | 2026-08-07 11:19 UTC | 1h 25m |
| 4XDAN |  | Bar Yehuda Airfield (LLMZ) | Bar Yehuda Airfield (LLMZ) | 2026-08-07 11:01 UTC | 2026-08-07 11:15 UTC | 14m |
| CHX26 | CHX | Wilhelmshaven-Mariensiel Airport (EDWI) | Wilhelmshaven-Mariensiel Airport (EDWI) | 2026-08-07 10:59 UTC | 2026-08-07 11:01 UTC | 2m |
| RGA06 | RGA | Locarno Airport (LSZL) | Muenster Aero Airport (LSPU) | 2026-08-07 10:50 UTC | 2026-08-07 11:00 UTC | 10m |
| N2114K |  | St Mary's County Regional Airport (K2W6) | Ocean City Municipal Airport (KOXB) | 2026-08-07 10:26 UTC | 2026-08-07 10:59 UTC | 32m |
| SVW11AA | SVW | Thessaloniki Macedonia International Airport (LGTS) | Mikonos Airport (LGMK) | 2026-08-07 10:12 UTC | 2026-08-07 10:55 UTC | 43m |
| N247EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-07 07:31 UTC | 2026-08-07 10:54 UTC | 3h 23m |
| ESF521 | ESF | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-07 08:09 UTC | 2026-08-07 10:53 UTC | 2h 43m |
| MOLOCH86 | MOL | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-07 10:49 UTC | 2026-08-07 10:52 UTC | 2m |
| N485LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-07 07:42 UTC | 2026-08-07 10:52 UTC | 3h 9m |
| AWQ176 | AWQ | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-08-07 10:34 UTC | 2026-08-07 10:49 UTC | 14m |
| DMHLG | DMH | Hetzleser Berg Airport (EDQX) | Hetzleser Berg Airport (EDQX) | 2026-08-07 10:42 UTC | 2026-08-07 10:44 UTC | 2m |
| MAS1276 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Termeloh Airport (WMBE) | 2026-08-07 10:33 UTC | 2026-08-07 10:44 UTC | 10m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | Leon Airport (LELN) | 2026-08-07 10:05 UTC | 2026-08-07 10:43 UTC | 38m |
| N92CJ |  | KI58 (KI58) | White Birch Airport (NK68) | 2026-08-07 07:38 UTC | 2026-08-07 10:43 UTC | 3h 4m |
| ANE1099 | ANE | Madrid Barajas International Airport (LEMD) | Bilbao Airport (LEBB) | 2026-08-07 10:07 UTC | 2026-08-07 10:41 UTC | 33m |
| DFC3ML | DFC | Rijeka Airport (LDRI) | Poznań-Ławica Airport (EPPO) | 2026-08-07 09:27 UTC | 2026-08-07 10:41 UTC | 1h 13m |
| FHKSI | FHK | Pribram Airport (LKPM) | Bolzano Airport (LIPB) | 2026-08-07 09:38 UTC | 2026-08-07 10:40 UTC | 1h 2m |
| SUI785 | SUI | Payerne Airport (LSMP) | Friedrichshafen Airport (EDNY) | 2026-08-07 10:03 UTC | 2026-08-07 10:40 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
