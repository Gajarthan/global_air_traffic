# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_20:09:11_UTC-green)

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

**Latest saved flight:** 2026-07-09 20:09:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-09 20:09:11 UTC

- **134,672** saved flights
- **45,557** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **134,672** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,620,457.6 tonnes** estimated CO2 emissions
- **93,939,570 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5469 |
| 2 | SkyWest Airlines | 4958 |
| 3 | EJA | 2635 |
| 4 | IndiGo | 2498 |
| 5 | American Airlines | 2107 |
| 6 | Southwest Airlines | 2026 |
| 7 | ENY | 1689 |
| 8 | Delta Air Lines | 1606 |
| 9 | Lufthansa | 1388 |
| 10 | LATAM Airlines | 1235 |
| 11 | Vueling | 1178 |
| 12 | WIF | 1173 |
| 13 | AZU | 1146 |
| 14 | LXJ | 1034 |
| 15 | AXM | 1021 |
| 16 | Swiss International | 956 |
| 17 | All Nippon Airways | 878 |
| 18 | easyJet | 875 |
| 19 | Alaska Airlines | 853 |
| 20 | QLK | 841 |
| 21 | EJU | 831 |
| 22 | VIV | 742 |
| 23 | AEE | 732 |
| 24 | CXK | 725 |
| 25 | Air France | 722 |
| 26 | Cathay Pacific | 721 |
| 27 | United Airlines | 712 |
| 28 | JetBlue | 709 |
| 29 | MXY | 697 |
| 30 | GLO | 685 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 115496 |
| 2 | 🇪🇸 ES | 8936 |
| 3 | 🇮🇳 IN | 7837 |
| 4 | 🇦🇺 AU | 7768 |
| 5 | 🇧🇷 BR | 7579 |
| 6 | 🇨🇦 CA | 7109 |
| 7 | 🇩🇪 DE | 7027 |
| 8 | 🇮🇹 IT | 6999 |
| 9 | 🇬🇧 GB | 6066 |
| 10 | 🇯🇵 JP | 5755 |
| 11 | 🇫🇷 FR | 5356 |
| 12 | 🇨🇴 CO | 4218 |
| 13 | 🇲🇽 MX | 3914 |
| 14 | 🇬🇷 GR | 3845 |
| 15 | 🇳🇴 NO | 3655 |
| 16 | 🇨🇭 CH | 3485 |
| 17 | 🇹🇷 TR | 3073 |
| 18 | 🇲🇾 MY | 2651 |
| 19 | 🇵🇱 PL | 2227 |
| 20 | 🇿🇦 ZA | 2217 |
| 21 | 🇳🇿 NZ | 2103 |
| 22 | 🇹🇭 TH | 2062 |
| 23 | 🇰🇷 KR | 1984 |
| 24 | 🇵🇭 PH | 1850 |
| 25 | 🇬🇹 GT | 1827 |
| 26 | 🇲🇦 MA | 1426 |
| 27 | 🇲🇪 ME | 1342 |
| 28 | 🇳🇱 NL | 1260 |
| 29 | 🇭🇷 HR | 1200 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2803 |
| 2 | Denver International Airport |  | US | 2274 |
| 3 | Tokyo International Airport |  | JP | 1878 |
| 4 | Indira Gandhi International Airport |  | IN | 1733 |
| 5 | Harry Reid International Airport |  | US | 1674 |
| 6 | Guaymaral Airport |  | CO | 1645 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1578 |
| 8 | Zurich Airport |  | CH | 1498 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1426 |
| 10 | La Aurora Airport |  | GT | 1412 |
| 11 | Frankfurt am Main International Airport |  | DE | 1343 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1297 |
| 13 | Chicago O'Hare International Airport |  | US | 1282 |
| 14 | Salt Lake City International Airport |  | US | 1196 |
| 15 | El Dorado International Airport |  | CO | 1194 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1165 |
| 18 | Madrid Barajas International Airport |  | ES | 1102 |
| 19 | Capua Airport |  | IT | 1102 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1100 |
| 21 | Congonhas Airport |  | BR | 1073 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 990 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 975 |
| 25 | Charles de Gaulle International Airport |  | FR | 963 |
| 26 | Bengaluru International Airport |  | IN | 944 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 924 |
| 28 | Malpensa International Airport |  | IT | 887 |
| 29 | Ninoy Aquino International Airport |  | PH | 861 |
| 30 | Daniel K Inouye International Airport |  | US | 837 |
| 31 | Barcelona International Airport |  | ES | 829 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 822 |
| 33 | Tenerife Norte Airport |  | ES | 807 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 789 |
| 35 | Calgary International Airport |  | CA | 779 |
| 36 | Scottsdale Airport |  | US | 769 |
| 37 | Seattle-Tacoma International Airport |  | US | 768 |
| 38 | Viracopos International Airport |  | BR | 767 |
| 39 | Vitoria/Foronda Airport |  | ES | 761 |
| 40 | Amsterdam Airport Schiphol |  | NL | 757 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 692 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 488 | 21m | 244 km | 2,054.8 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 338 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 324 | 1h 10m | 770 km | 4,304.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 288 | 14m | 114 km | 564.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 244 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 198 | 22m | 55 km | 188.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 187 | 26m | 215 km | 692.6 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 182 | 1h 46m | 1,423 km | 4,466.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 180 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 163 | 20m | 250 km | 704.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 160 | 44m | 452 km | 1,247.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 156 | 1h 16m | 961 km | 2,585.8 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 154 | 1h 38m | 1,156 km | 3,072.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DAL3095 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | 20SC (20SC) | 2026-07-09 19:41 UTC | 2026-07-09 20:09 UTC | 27m |
| N850UW |  | Fountain Prairie Airport (6WN6) | Dane County Regional/Truax Field (KMSN) | 2026-07-09 19:50 UTC | 2026-07-09 20:08 UTC | 18m |
| TKR912 | TKR | Grant County International Airport (KMWH) | Quail Field (OG42) | 2026-07-09 19:49 UTC | 2026-07-09 20:05 UTC | 16m |
| N474SM |  | Camarillo Airport (KCMA) | Bob Maxwell Memorial Airfield (KOKB) | 2026-07-09 18:58 UTC | 2026-07-09 20:05 UTC | 1h 6m |
| JBU2454 | JetBlue | Ronald Reagan Washington Ntl Airport (KDCA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-09 18:53 UTC | 2026-07-09 20:02 UTC | 1h 9m |
| N4347R |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-07-09 19:34 UTC | 2026-07-09 19:59 UTC | 24m |
| AAL1846 | American Airlines | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-09 16:22 UTC | 2026-07-09 19:58 UTC | 3h 36m |
| N535LE |  | West Houston Airport (KIWS) | West Houston Airport (KIWS) | 2026-07-09 19:50 UTC | 2026-07-09 19:57 UTC | 7m |
| N427EF |  | Lake Tahoe Airport (KTVL) | Mc Clellan Airfield (KMCC) | 2026-07-09 19:36 UTC | 2026-07-09 19:57 UTC | 21m |
| FFT187 | FFT | Orlando International Airport (KMCO) | La Aurora Airport (MGGT) | 2026-07-09 17:33 UTC | 2026-07-09 19:56 UTC | 2h 22m |
| RAM911T | Royal Air Maroc | Istanbul Airport (LTFM) | Ben Slimane Airport (GMMB) | 2026-07-09 15:52 UTC | 2026-07-09 19:56 UTC | 4h 3m |
| N900BA |  | Joe Foss Field (KFSD) | Wadena Municipal Airport (KADC) | 2026-07-09 19:14 UTC | 2026-07-09 19:52 UTC | 38m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Zhuhai Airport (ZGSD) | 2026-07-09 05:47 UTC | 2026-07-09 19:51 UTC | 14h 4m |
| N41HX |  | Blanding Municipal Airport (KBDG) | Blanding Municipal Airport (KBDG) | 2026-07-09 19:11 UTC | 2026-07-09 19:51 UTC | 39m |
| N1910R |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-07-09 19:39 UTC | 2026-07-09 19:51 UTC | 12m |
| N1947F |  | Melbourne Orlando International Airport (KMLB) | Valkaria Airport (KX59) | 2026-07-09 19:18 UTC | 2026-07-09 19:50 UTC | 32m |
| HKC372 | HKC | Singapore Changi International Airport (WSSS) | Zhuhai Airport (ZGSD) | 2026-07-09 13:21 UTC | 2026-07-09 19:50 UTC | 6h 29m |
| EJA959 | EJA | Victoria International Airport (CYYJ) | Boeing Field/King County International Airport (KBFI) | 2026-07-09 19:29 UTC | 2026-07-09 19:50 UTC | 20m |
| AAL755 | American Airlines | Charles de Gaulle International Airport (LFPG) | Philadelphia International Airport (KPHL) | 2026-07-09 12:21 UTC | 2026-07-09 19:49 UTC | 7h 27m |
| N71PW |  | Eagle Field (15ME) | Presque Isle International Airport (KPQI) | 2026-07-09 18:57 UTC | 2026-07-09 19:46 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
