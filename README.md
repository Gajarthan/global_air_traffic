# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_12:43:55_UTC-green)

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

**Latest saved flight:** 2026-07-30 12:43:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 12:43:55 UTC

- **160,193** saved flights
- **52,966** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **160,193** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,923,672.2 tonnes** estimated CO2 emissions
- **111,517,231 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6425 |
| 2 | SkyWest Airlines | 5837 |
| 3 | EJA | 3176 |
| 4 | IndiGo | 2824 |
| 5 | American Airlines | 2531 |
| 6 | Southwest Airlines | 2511 |
| 7 | ENY | 1994 |
| 8 | Delta Air Lines | 1904 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1504 |
| 11 | AZU | 1410 |
| 12 | WIF | 1357 |
| 13 | Vueling | 1336 |
| 14 | LXJ | 1234 |
| 15 | AXM | 1120 |
| 16 | Swiss International | 1108 |
| 17 | easyJet | 1047 |
| 18 | Alaska Airlines | 1001 |
| 19 | QLK | 991 |
| 20 | All Nippon Airways | 990 |
| 21 | EJU | 981 |
| 22 | VIV | 879 |
| 23 | CXK | 847 |
| 24 | United Airlines | 847 |
| 25 | Cathay Pacific | 845 |
| 26 | GLO | 844 |
| 27 | AEE | 843 |
| 28 | Air France | 836 |
| 29 | MXY | 832 |
| 30 | JetBlue | 820 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 138139 |
| 2 | 🇪🇸 ES | 10278 |
| 3 | 🇧🇷 BR | 9157 |
| 4 | 🇦🇺 AU | 9074 |
| 5 | 🇮🇳 IN | 8883 |
| 6 | 🇨🇦 CA | 8701 |
| 7 | 🇮🇹 IT | 8271 |
| 8 | 🇩🇪 DE | 8108 |
| 9 | 🇬🇧 GB | 7357 |
| 10 | 🇯🇵 JP | 6529 |
| 11 | 🇫🇷 FR | 6339 |
| 12 | 🇨🇴 CO | 5650 |
| 13 | 🇬🇷 GR | 4596 |
| 14 | 🇲🇽 MX | 4592 |
| 15 | 🇳🇴 NO | 4240 |
| 16 | 🇨🇭 CH | 4196 |
| 17 | 🇹🇷 TR | 3826 |
| 18 | 🇲🇾 MY | 2908 |
| 19 | 🇵🇱 PL | 2724 |
| 20 | 🇿🇦 ZA | 2589 |
| 21 | 🇳🇿 NZ | 2362 |
| 22 | 🇹🇭 TH | 2292 |
| 23 | 🇵🇭 PH | 2116 |
| 24 | 🇰🇷 KR | 2107 |
| 25 | 🇬🇹 GT | 2040 |
| 26 | 🇲🇦 MA | 1623 |
| 27 | 🇲🇪 ME | 1526 |
| 28 | 🇭🇷 HR | 1494 |
| 29 | 🇳🇱 NL | 1470 |
| 30 | 🇲🇴 MO | 1334 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3270 |
| 2 | Denver International Airport |  | US | 2663 |
| 3 | Tokyo International Airport |  | JP | 2063 |
| 4 | Guaymaral Airport |  | CO | 2006 |
| 5 | Indira Gandhi International Airport |  | IN | 1975 |
| 6 | Harry Reid International Airport |  | US | 1951 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1775 |
| 8 | Zurich Airport |  | CH | 1716 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1682 |
| 10 | La Aurora Airport |  | GT | 1583 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1493 |
| 12 | El Dorado International Airport |  | CO | 1468 |
| 13 | Frankfurt am Main International Airport |  | DE | 1466 |
| 14 | Chicago O'Hare International Airport |  | US | 1451 |
| 15 | Salt Lake City International Airport |  | US | 1440 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1337 |
| 17 | Macau International Airport |  | MO | 1334 |
| 18 | Congonhas Airport |  | BR | 1331 |
| 19 | Madrid Barajas International Airport |  | ES | 1270 |
| 20 | Capua Airport |  | IT | 1260 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1229 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1147 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1137 |
| 24 | Charlotte/Douglas International Airport |  | US | 1122 |
| 25 | Kuala Lumpur International Airport |  | MY | 1111 |
| 26 | Charles de Gaulle International Airport |  | FR | 1101 |
| 27 | Malpensa International Airport |  | IT | 1063 |
| 28 | Bengaluru International Airport |  | IN | 1056 |
| 29 | Ninoy Aquino International Airport |  | PH | 992 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 977 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 976 |
| 32 | Barcelona International Airport |  | ES | 956 |
| 33 | Daniel K Inouye International Airport |  | US | 945 |
| 34 | Seattle-Tacoma International Airport |  | US | 935 |
| 35 | Calgary International Airport |  | CA | 921 |
| 36 | Viracopos International Airport |  | BR | 916 |
| 37 | Scottsdale Airport |  | US | 904 |
| 38 | Tenerife Norte Airport |  | ES | 899 |
| 39 | Oslo Gardermoen Airport |  | NO | 891 |
| 40 | Amsterdam Airport Schiphol |  | NL | 884 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 842 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 584 | 21m | 244 km | 2,459.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 379 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 369 | 1h 9m | 770 km | 4,901.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 294 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 281 | 27m | 275 km | 1,331.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 228 | 44m | 241 km | 947.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 220 | 1h 47m | 1,423 km | 5,399.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 202 | 20m | 250 km | 872.5 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 192 | 30m | 49 km | 162.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 190 | 18m | 144 km | 472.6 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 182 | 50m | 556 km | 1,744.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 179 | 1h 39m | 1,156 km | 3,571.0 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 177 | 1h 1m | 695 km | 2,121.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 170 | 23m | 218 km | 640.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LFA330 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-07-30 12:21 UTC | 2026-07-30 12:43 UTC | 22m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-30 12:29 UTC | 2026-07-30 12:39 UTC | 10m |
| N802JL |  | IA17 (IA17) | IA17 (IA17) | 2026-07-30 12:03 UTC | 2026-07-30 12:39 UTC | 35m |
| GRYDR76 | GRY | Albany International Airport (KALB) | Laguardia Airport (KLGA) | 2026-07-30 11:40 UTC | 2026-07-30 12:39 UTC | 58m |
| HB3275 |  | Muenster Aero Airport (LSPU) | Samedan Airport (LSZS) | 2026-07-30 10:49 UTC | 2026-07-30 12:35 UTC | 1h 45m |
| N682SA |  | Baggett Airport (FD57) | Naples Municipal Airport (KAPF) | 2026-07-30 11:09 UTC | 2026-07-30 12:19 UTC | 1h 10m |
| HBZVQ | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-07-30 11:58 UTC | 2026-07-30 12:18 UTC | 19m |
| EIEMU | EIE | Weston Airport (EIWT) | Weston Airport (EIWT) | 2026-07-30 11:21 UTC | 2026-07-30 12:13 UTC | 51m |
| VAG130 | VAG | Suvarnabhumi Airport (VTBS) | Noi Bai International Airport (VVNB) | 2026-07-30 07:49 UTC | 2026-07-30 12:07 UTC | 4h 18m |
| EIN205 | Aer Lingus | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-07-30 11:27 UTC | 2026-07-30 12:07 UTC | 39m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-07-29 21:41 UTC | 2026-07-30 12:06 UTC | 14h 25m |
| EDL1 | EDL | EDJG (EDJG) | EDJG (EDJG) | 2026-07-30 11:39 UTC | 2026-07-30 12:06 UTC | 26m |
| N59FG |  | Sacramento Executive Airport (KSAC) | Rogers Field (KO05) | 2026-07-30 11:08 UTC | 2026-07-30 12:05 UTC | 57m |
| N226DH |  | J Maddock Airport (IL38) | J Maddock Airport (IL38) | 2026-07-30 12:02 UTC | 2026-07-30 12:05 UTC | 2m |
| THY6238 | Turkish Airlines | Tbilisi International Airport (UGTB) | Macau International Airport (VMMC) | 2026-07-30 04:00 UTC | 2026-07-30 12:04 UTC | 8h 4m |
| N2810U |  | Fort Lauderdale Executive Airport (KFXE) | Fort Lauderdale Executive Airport (KFXE) | 2026-07-30 11:57 UTC | 2026-07-30 12:04 UTC | 7m |
| N470MM |  | Bishman Airport (90MN) | Flying Cloud Airport (KFCM) | 2026-07-30 11:39 UTC | 2026-07-30 12:03 UTC | 23m |
| EMO75 | EMO | Farnborough Airport (EGLF) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-30 10:13 UTC | 2026-07-30 12:03 UTC | 1h 49m |
| SUCCG | SUC | El Nouzha Airport (HEAX) | El Nouzha Airport (HEAX) | 2026-07-30 11:50 UTC | 2026-07-30 11:59 UTC | 9m |
| PAV430 | PAV | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | Samedan Airport (LSZS) | 2026-07-30 11:05 UTC | 2026-07-30 11:59 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
