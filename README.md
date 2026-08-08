# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_18:10:39_UTC-green)

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

**Latest saved flight:** 2026-08-08 18:10:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 18:10:39 UTC

- **179,128** saved flights
- **57,481** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **179,128** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,152,293.4 tonnes** estimated CO2 emissions
- **124,770,632 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7103 |
| 2 | SkyWest Airlines | 6525 |
| 3 | EJA | 3525 |
| 4 | IndiGo | 3144 |
| 5 | Southwest Airlines | 2817 |
| 6 | American Airlines | 2786 |
| 7 | ENY | 2231 |
| 8 | Delta Air Lines | 2119 |
| 9 | LATAM Airlines | 1667 |
| 10 | Lufthansa | 1600 |
| 11 | AZU | 1598 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1481 |
| 14 | LXJ | 1401 |
| 15 | Swiss International | 1224 |
| 16 | easyJet | 1216 |
| 17 | AXM | 1210 |
| 18 | EJU | 1093 |
| 19 | QLK | 1093 |
| 20 | All Nippon Airways | 1088 |
| 21 | Alaska Airlines | 1082 |
| 22 | VIV | 984 |
| 23 | GLO | 953 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 945 |
| 26 | AEE | 932 |
| 27 | Air France | 920 |
| 28 | United Airlines | 920 |
| 29 | MXY | 898 |
| 30 | PGT | 888 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 153597 |
| 2 | 🇪🇸 ES | 11498 |
| 3 | 🇧🇷 BR | 10259 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9854 |
| 6 | 🇨🇦 CA | 9765 |
| 7 | 🇮🇹 IT | 9256 |
| 8 | 🇩🇪 DE | 8879 |
| 9 | 🇬🇧 GB | 8272 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7136 |
| 12 | 🇨🇴 CO | 6618 |
| 13 | 🇬🇷 GR | 5224 |
| 14 | 🇲🇽 MX | 5121 |
| 15 | 🇨🇭 CH | 4782 |
| 16 | 🇳🇴 NO | 4640 |
| 17 | 🇹🇷 TR | 4534 |
| 18 | 🇲🇾 MY | 3159 |
| 19 | 🇵🇱 PL | 2993 |
| 20 | 🇿🇦 ZA | 2922 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2287 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1812 |
| 27 | 🇭🇷 HR | 1781 |
| 28 | 🇲🇪 ME | 1633 |
| 29 | 🇳🇱 NL | 1613 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3694 |
| 2 | Denver International Airport |  | US | 2959 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Guaymaral Airport |  | CO | 2203 |
| 5 | Indira Gandhi International Airport |  | IN | 2194 |
| 6 | Harry Reid International Airport |  | US | 2117 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1930 |
| 8 | Zurich Airport |  | CH | 1906 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1866 |
| 10 | La Aurora Airport |  | GT | 1758 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1635 |
| 12 | Chicago O'Hare International Airport |  | US | 1615 |
| 13 | Salt Lake City International Airport |  | US | 1600 |
| 14 | El Dorado International Airport |  | CO | 1595 |
| 15 | Frankfurt am Main International Airport |  | DE | 1563 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1488 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1433 |
| 19 | Capua Airport |  | IT | 1401 |
| 20 | Madrid Barajas International Airport |  | ES | 1400 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1335 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1274 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1229 |
| 25 | Charlotte/Douglas International Airport |  | US | 1219 |
| 26 | Charles de Gaulle International Airport |  | FR | 1212 |
| 27 | Kuala Lumpur International Airport |  | MY | 1190 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1110 |
| 30 | Ninoy Aquino International Airport |  | PH | 1109 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1099 |
| 32 | Barcelona International Airport |  | ES | 1064 |
| 33 | Daniel K Inouye International Airport |  | US | 1029 |
| 34 | Seattle-Tacoma International Airport |  | US | 1029 |
| 35 | Viracopos International Airport |  | BR | 1027 |
| 36 | Reno/Tahoe International Airport |  | US | 1019 |
| 37 | Calgary International Airport |  | CA | 1017 |
| 38 | Oslo Gardermoen Airport |  | NO | 995 |
| 39 | Tenerife Norte Airport |  | ES | 981 |
| 40 | Amsterdam Airport Schiphol |  | NL | 971 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 910 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 659 | 21m | 244 km | 2,774.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 300 | 27m | 275 km | 1,421.6 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 251 | 1h 48m | 1,423 km | 6,159.9 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 235 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 216 | 51m | 556 km | 2,070.5 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 215 | 1h 15m | 961 km | 3,563.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 213 | 19m | 144 km | 529.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 204 | 24m | 218 km | 768.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 202 | 28m | 152 km | 527.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 195 | 1h 2m | 695 km | 2,337.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N52450 |  | Bolingbrook's Clow International Airport (K1C5) | Aurora Municipal Airport (KARR) | 2026-08-08 17:24 UTC | 2026-08-08 18:10 UTC | 45m |
| N1033A |  | Plant City Airport (KPCM) | Plant City Airport (KPCM) | 2026-08-08 17:30 UTC | 2026-08-08 18:10 UTC | 39m |
| JUMP4 | JUM | Carson Field (MT53) | Carson Field (MT53) | 2026-08-08 17:53 UTC | 2026-08-08 18:03 UTC | 10m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-08-08 17:48 UTC | 2026-08-08 18:01 UTC | 13m |
| N202LS |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-08-08 17:14 UTC | 2026-08-08 18:00 UTC | 45m |
| THY4YM | Turkish Airlines | Istanbul Airport (LTFM) | HE42 (HE42) | 2026-08-08 16:28 UTC | 2026-08-08 18:00 UTC | 1h 32m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-08-08 17:26 UTC | 2026-08-08 18:00 UTC | 34m |
| BRG621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-08-08 17:13 UTC | 2026-08-08 17:59 UTC | 45m |
| N405CM |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-08 17:40 UTC | 2026-08-08 17:56 UTC | 16m |
| WML74 | WML | Washington Manassas/Harry P Davis Field (KHEF) | Ocean City Municipal Airport (KOXB) | 2026-08-08 17:17 UTC | 2026-08-08 17:53 UTC | 35m |
| N735QM |  | Lodi Airport (K1O3) | Lake Tahoe Airport (KTVL) | 2026-08-08 17:13 UTC | 2026-08-08 17:53 UTC | 40m |
| MSR798 | EgyptAir | Vienna International Airport (LOWW) | HE12 (HE12) | 2026-08-08 15:02 UTC | 2026-08-08 17:51 UTC | 2h 48m |
| CXK297 | CXK | Ogden-Hinckley Airport (KOGD) | Ogden-Hinckley Airport (KOGD) | 2026-08-08 17:42 UTC | 2026-08-08 17:45 UTC | 3m |
| N239DC |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-08 17:30 UTC | 2026-08-08 17:45 UTC | 14m |
| DCM2700 | DCM | Dyess Afb Airport (KDYS) | Flying H Ranch Airport (68NM) | 2026-08-08 17:04 UTC | 2026-08-08 17:43 UTC | 39m |
| UBG307 | UBG | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-08-08 16:39 UTC | 2026-08-08 17:40 UTC | 1h 0m |
| N54855 |  | Double W Airport (3OK7) | Tulsa International Airport (KTUL) | 2026-08-08 17:19 UTC | 2026-08-08 17:40 UTC | 21m |
| N457TL |  | Skypark Airport (KBTF) | Skypark Airport (KBTF) | 2026-08-08 16:46 UTC | 2026-08-08 17:36 UTC | 50m |
| N15MJ |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-08 17:01 UTC | 2026-08-08 17:36 UTC | 34m |
| BOE751 | BOE | Boeing Field/King County International Airport (KBFI) | 74WA (74WA) | 2026-08-08 16:28 UTC | 2026-08-08 17:34 UTC | 1h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
