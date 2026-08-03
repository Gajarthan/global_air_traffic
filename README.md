# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_23:17:08_UTC-green)

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

**Latest saved flight:** 2026-08-03 23:17:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 23:17:08 UTC

- **169,641** saved flights
- **55,344** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **169,641** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,044,789.2 tonnes** estimated CO2 emissions
- **118,538,506 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6760 |
| 2 | SkyWest Airlines | 6214 |
| 3 | EJA | 3372 |
| 4 | IndiGo | 2981 |
| 5 | American Airlines | 2677 |
| 6 | Southwest Airlines | 2674 |
| 7 | ENY | 2121 |
| 8 | Delta Air Lines | 2023 |
| 9 | LATAM Airlines | 1575 |
| 10 | Lufthansa | 1557 |
| 11 | AZU | 1495 |
| 12 | WIF | 1419 |
| 13 | Vueling | 1398 |
| 14 | LXJ | 1334 |
| 15 | AXM | 1166 |
| 16 | Swiss International | 1159 |
| 17 | easyJet | 1139 |
| 18 | EJU | 1039 |
| 19 | Alaska Airlines | 1037 |
| 20 | QLK | 1029 |
| 21 | All Nippon Airways | 1023 |
| 22 | VIV | 935 |
| 23 | Cathay Pacific | 908 |
| 24 | CXK | 898 |
| 25 | United Airlines | 896 |
| 26 | GLO | 890 |
| 27 | AEE | 887 |
| 28 | Air France | 871 |
| 29 | MXY | 868 |
| 30 | JetBlue | 853 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 146381 |
| 2 | 🇪🇸 ES | 10868 |
| 3 | 🇧🇷 BR | 9658 |
| 4 | 🇦🇺 AU | 9429 |
| 5 | 🇮🇳 IN | 9339 |
| 6 | 🇨🇦 CA | 9209 |
| 7 | 🇮🇹 IT | 8749 |
| 8 | 🇩🇪 DE | 8445 |
| 9 | 🇬🇧 GB | 7875 |
| 10 | 🇯🇵 JP | 6789 |
| 11 | 🇫🇷 FR | 6714 |
| 12 | 🇨🇴 CO | 6166 |
| 13 | 🇬🇷 GR | 4924 |
| 14 | 🇲🇽 MX | 4858 |
| 15 | 🇨🇭 CH | 4463 |
| 16 | 🇳🇴 NO | 4426 |
| 17 | 🇹🇷 TR | 4114 |
| 18 | 🇲🇾 MY | 3035 |
| 19 | 🇵🇱 PL | 2859 |
| 20 | 🇿🇦 ZA | 2743 |
| 21 | 🇹🇭 TH | 2459 |
| 22 | 🇳🇿 NZ | 2458 |
| 23 | 🇵🇭 PH | 2235 |
| 24 | 🇬🇹 GT | 2190 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1713 |
| 27 | 🇭🇷 HR | 1634 |
| 28 | 🇲🇪 ME | 1565 |
| 29 | 🇳🇱 NL | 1540 |
| 30 | 🇲🇴 MO | 1442 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3497 |
| 2 | Denver International Airport |  | US | 2819 |
| 3 | Tokyo International Airport |  | JP | 2133 |
| 4 | Guaymaral Airport |  | CO | 2107 |
| 5 | Indira Gandhi International Airport |  | IN | 2071 |
| 6 | Harry Reid International Airport |  | US | 2043 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1855 |
| 8 | Zurich Airport |  | CH | 1799 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1791 |
| 10 | La Aurora Airport |  | GT | 1690 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1566 |
| 12 | El Dorado International Airport |  | CO | 1544 |
| 13 | Chicago O'Hare International Airport |  | US | 1543 |
| 14 | Salt Lake City International Airport |  | US | 1524 |
| 15 | Frankfurt am Main International Airport |  | DE | 1518 |
| 16 | Macau International Airport |  | MO | 1442 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1400 |
| 18 | Congonhas Airport |  | BR | 1388 |
| 19 | Madrid Barajas International Airport |  | ES | 1333 |
| 20 | Capua Airport |  | IT | 1321 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1287 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1202 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1184 |
| 24 | Charlotte/Douglas International Airport |  | US | 1181 |
| 25 | Charles de Gaulle International Airport |  | FR | 1151 |
| 26 | Kuala Lumpur International Airport |  | MY | 1144 |
| 27 | Malpensa International Airport |  | IT | 1142 |
| 28 | Bengaluru International Airport |  | IN | 1109 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1053 |
| 30 | Ninoy Aquino International Airport |  | PH | 1051 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1048 |
| 32 | Barcelona International Airport |  | ES | 1005 |
| 33 | Daniel K Inouye International Airport |  | US | 985 |
| 34 | Seattle-Tacoma International Airport |  | US | 982 |
| 35 | Viracopos International Airport |  | BR | 965 |
| 36 | Calgary International Airport |  | CA | 962 |
| 37 | Reno/Tahoe International Airport |  | US | 952 |
| 38 | Tenerife Norte Airport |  | ES | 943 |
| 39 | Oslo Gardermoen Airport |  | NO | 941 |
| 40 | Scottsdale Airport |  | US | 936 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 875 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 618 | 21m | 244 km | 2,602.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 403 | 24m | 225 km | 1,563.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 403 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 289 | 27m | 275 km | 1,369.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 251 | 44m | 241 km | 1,042.6 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 233 | 1h 47m | 1,423 km | 5,718.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 215 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 202 | 19m | 144 km | 502.5 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 201 | 50m | 556 km | 1,926.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 200 | 1h 15m | 961 km | 3,315.1 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 190 | 1h 38m | 1,156 km | 3,790.4 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 187 | 24m | 218 km | 704.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 183 | 8m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N904RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-03 22:33 UTC | 2026-08-03 23:17 UTC | 43m |
| ROC | ROC | Redcliffe Airport (YRED) | Sunshine Coast Airport (YBMC) | 2026-08-03 22:55 UTC | 2026-08-03 23:16 UTC | 21m |
| RAQ | RAQ | Redcliffe Airport (YRED) | Brisbane Archerfield Airport (YBAF) | 2026-08-03 22:51 UTC | 2026-08-03 23:09 UTC | 17m |
| LRS1010 | LRS | Juan Santamaria International Airport (MROC) | Tambor Airport (MRTR) | 2026-08-03 22:43 UTC | 2026-08-03 23:04 UTC | 21m |
| N3181Q |  | Fulton County Executive/Charlie Brown Field (KFTY) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-03 22:34 UTC | 2026-08-03 23:03 UTC | 29m |
| EYI | EYI | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-08-03 22:48 UTC | 2026-08-03 23:02 UTC | 14m |
| YNW | YNW | Toowoomba Airport (YTWB) | Brisbane Archerfield Airport (YBAF) | 2026-08-03 22:26 UTC | 2026-08-03 23:02 UTC | 35m |
| KEN46 | KEN | Astoria Regional Airport (KAST) | Boeing Field/King County International Airport (KBFI) | 2026-08-03 22:27 UTC | 2026-08-03 23:00 UTC | 32m |
| CLX1728 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-08-03 12:10 UTC | 2026-08-03 22:58 UTC | 10h 47m |
| N205FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-03 22:03 UTC | 2026-08-03 22:51 UTC | 48m |
| CODE21 | COD | Sopwith Ldg Airport (OK56) | Sopwith Ldg Airport (OK56) | 2026-08-03 22:30 UTC | 2026-08-03 22:50 UTC | 19m |
| N266AG |  | Middleton Municipal/Morey Field (KC29) | Morrisonville International Airport (WN85) | 2026-08-03 12:21 UTC | 2026-08-03 22:47 UTC | 10h 26m |
| TWY381 | TWY | Norman Y Mineta San Jose International Airport (KSJC) | Sacramento Mather Airport (KMHR) | 2026-08-03 22:21 UTC | 2026-08-03 22:47 UTC | 26m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-08-03 12:10 UTC | 2026-08-03 22:46 UTC | 10h 36m |
| N1308T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-03 21:54 UTC | 2026-08-03 22:46 UTC | 52m |
| ROKT61 | ROK | 5MS2 (5MS2) | Dean Griffin Memorial Airport (KM24) | 2026-08-03 22:28 UTC | 2026-08-03 22:41 UTC | 13m |
| CFTLU | CFT | CNQ4 (CNQ4) | CNQ4 (CNQ4) | 2026-08-03 22:19 UTC | 2026-08-03 22:41 UTC | 21m |
| N43685 |  | Atlanta Regional Falcon Field (KFFC) | K4A7 (K4A7) | 2026-08-03 22:20 UTC | 2026-08-03 22:38 UTC | 18m |
| N5005R |  | Aurora Municipal Airport (KARR) | 0IL8 (0IL8) | 2026-08-03 22:30 UTC | 2026-08-03 22:37 UTC | 7m |
| N2530B |  | Owosso Community Airport (KRNP) | 46MI (46MI) | 2026-08-03 21:53 UTC | 2026-08-03 22:37 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
