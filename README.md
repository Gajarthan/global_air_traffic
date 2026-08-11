# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_07:34:52_UTC-green)

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

**Latest saved flight:** 2026-08-11 07:34:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 07:34:52 UTC

- **186,057** saved flights
- **59,054** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **186,057** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,232,115.5 tonnes** estimated CO2 emissions
- **129,398,001 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7364 |
| 2 | SkyWest Airlines | 6785 |
| 3 | EJA | 3676 |
| 4 | IndiGo | 3246 |
| 5 | Southwest Airlines | 2925 |
| 6 | American Airlines | 2901 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2192 |
| 9 | LATAM Airlines | 1740 |
| 10 | AZU | 1673 |
| 11 | Lufthansa | 1631 |
| 12 | WIF | 1538 |
| 13 | Vueling | 1531 |
| 14 | LXJ | 1459 |
| 15 | easyJet | 1271 |
| 16 | Swiss International | 1269 |
| 17 | AXM | 1243 |
| 18 | QLK | 1151 |
| 19 | EJU | 1148 |
| 20 | All Nippon Airways | 1139 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1027 |
| 23 | GLO | 997 |
| 24 | AEE | 963 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | PGT | 951 |
| 28 | United Airlines | 950 |
| 29 | Cathay Pacific | 947 |
| 30 | MXY | 922 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159071 |
| 2 | 🇪🇸 ES | 11918 |
| 3 | 🇧🇷 BR | 10680 |
| 4 | 🇦🇺 AU | 10428 |
| 5 | 🇮🇳 IN | 10174 |
| 6 | 🇨🇦 CA | 10168 |
| 7 | 🇮🇹 IT | 9597 |
| 8 | 🇩🇪 DE | 9165 |
| 9 | 🇬🇧 GB | 8614 |
| 10 | 🇯🇵 JP | 7587 |
| 11 | 🇫🇷 FR | 7410 |
| 12 | 🇨🇴 CO | 7026 |
| 13 | 🇬🇷 GR | 5442 |
| 14 | 🇲🇽 MX | 5320 |
| 15 | 🇨🇭 CH | 4957 |
| 16 | 🇹🇷 TR | 4885 |
| 17 | 🇳🇴 NO | 4776 |
| 18 | 🇲🇾 MY | 3248 |
| 19 | 🇿🇦 ZA | 3120 |
| 20 | 🇵🇱 PL | 3094 |
| 21 | 🇹🇭 TH | 2879 |
| 22 | 🇳🇿 NZ | 2662 |
| 23 | 🇵🇭 PH | 2458 |
| 24 | 🇬🇹 GT | 2375 |
| 25 | 🇰🇷 KR | 2305 |
| 26 | 🇲🇦 MA | 1879 |
| 27 | 🇭🇷 HR | 1870 |
| 28 | 🇲🇪 ME | 1670 |
| 29 | 🇳🇱 NL | 1659 |
| 30 | 🇲🇴 MO | 1522 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3865 |
| 2 | Denver International Airport |  | US | 3069 |
| 3 | Tokyo International Airport |  | JP | 2348 |
| 4 | Indira Gandhi International Airport |  | IN | 2288 |
| 5 | Guaymaral Airport |  | CO | 2273 |
| 6 | Harry Reid International Airport |  | US | 2182 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1985 |
| 8 | Zurich Airport |  | CH | 1981 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1931 |
| 10 | La Aurora Airport |  | GT | 1822 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1672 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1599 |
| 16 | Congonhas Airport |  | BR | 1553 |
| 17 | Macau International Airport |  | MO | 1522 |
| 18 | Madrid Barajas International Airport |  | ES | 1461 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1454 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1389 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1330 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1302 |
| 24 | Malpensa International Airport |  | IT | 1282 |
| 25 | Charles de Gaulle International Airport |  | FR | 1266 |
| 26 | Charlotte/Douglas International Airport |  | US | 1256 |
| 27 | Kuala Lumpur International Airport |  | MY | 1217 |
| 28 | Bengaluru International Airport |  | IN | 1202 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1167 |
| 30 | Ninoy Aquino International Airport |  | PH | 1160 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1143 |
| 32 | Barcelona International Airport |  | ES | 1099 |
| 33 | Reno/Tahoe International Airport |  | US | 1073 |
| 34 | Seattle-Tacoma International Airport |  | US | 1073 |
| 35 | Viracopos International Airport |  | BR | 1070 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1036 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1006 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 450 | 1h 7m | 770 km | 5,977.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 434 | 24m | 225 km | 1,683.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 312 | 27m | 275 km | 1,478.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 279 | 44m | 241 km | 1,158.9 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 265 | 1h 49m | 1,423 km | 6,503.5 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 250 | 20m | 250 km | 1,079.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 232 | 27m | 215 km | 859.2 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 221 | 1h 38m | 1,156 km | 4,408.9 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 217 | 31m | 369 km | 1,381.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| POE319 | POE | Toronto Pearson International Airport (CYYZ) | Vancouver International Airport (CYVR) | 2026-08-11 02:30 UTC | 2026-08-11 07:34 UTC | 5h 4m |
| DRAG168 | DRA | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Belluno Airport (LIDB) | 2026-08-11 07:00 UTC | 2026-08-11 07:30 UTC | 29m |
| NHZ34 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-08-11 06:59 UTC | 2026-08-11 07:26 UTC | 26m |
| DHK800P | DHK | Belfast International Airport (EGAA) | East Midlands Airport (EGNX) | 2026-08-11 06:40 UTC | 2026-08-11 07:21 UTC | 41m |
| VSB92 | VSB | Barrow Walney Island Airport (EGNL) | Bristol International Airport (EGGD) | 2026-08-11 06:36 UTC | 2026-08-11 07:11 UTC | 34m |
| RYR72GT | Ryanair | Kaunas International Airport (EYKA) | Dublin Airport (EIDW) | 2026-08-11 03:48 UTC | 2026-08-11 06:52 UTC | 3h 4m |
| HBKGP | HBK | Bern Belp Airport (LSZB) | Bern Belp Airport (LSZB) | 2026-08-11 06:43 UTC | 2026-08-11 06:49 UTC | 6m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-11 06:11 UTC | 2026-08-11 06:47 UTC | 36m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-11 05:43 UTC | 2026-08-11 06:39 UTC | 55m |
| LR455 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-08-11 06:02 UTC | 2026-08-11 06:38 UTC | 36m |
| CXI38SB | CXI | Vienna International Airport (LOWW) | Vienna International Airport (LOWW) | 2026-08-11 06:16 UTC | 2026-08-11 06:37 UTC | 21m |
| WIF2B | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-11 05:47 UTC | 2026-08-11 06:36 UTC | 48m |
| N410W |  | Frasca Field (KC16) | Frasca Field (KC16) | 2026-08-11 06:28 UTC | 2026-08-11 06:32 UTC | 4m |
| CEB909 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-11 06:07 UTC | 2026-08-11 06:29 UTC | 22m |
| WIF37H | WIF | Bergen Airport Flesland (ENBR) | Kristiansand Airport (ENCN) | 2026-08-11 05:51 UTC | 2026-08-11 06:25 UTC | 33m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-08-11 05:38 UTC | 2026-08-11 06:24 UTC | 46m |
| AXM6496 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-08-11 06:11 UTC | 2026-08-11 06:24 UTC | 12m |
| AZU4112 | AZU | Val de Cans/Julio Cezar Ribeiro International Airport (SBBE) | Maraba Airport (SBMA) | 2026-08-11 05:43 UTC | 2026-08-11 06:23 UTC | 40m |
| VT131RK |  | Faa'a International Airport (NTAA) | Tikehau Airport (NTGC) | 2026-08-11 05:34 UTC | 2026-08-11 06:17 UTC | 43m |
| OC77 |  | Nagasaki Airport (RJFU) | Kamigoto Airport (RJDK) | 2026-08-11 06:11 UTC | 2026-08-11 06:17 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
