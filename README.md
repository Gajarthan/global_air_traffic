# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_09:21:45_UTC-green)

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

**Latest saved flight:** 2026-08-11 09:21:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 09:21:45 UTC

- **186,270** saved flights
- **59,092** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **186,270** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,235,045.0 tonnes** estimated CO2 emissions
- **129,567,827 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7381 |
| 2 | SkyWest Airlines | 6785 |
| 3 | EJA | 3676 |
| 4 | IndiGo | 3252 |
| 5 | Southwest Airlines | 2925 |
| 6 | American Airlines | 2902 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2193 |
| 9 | LATAM Airlines | 1740 |
| 10 | AZU | 1673 |
| 11 | Lufthansa | 1634 |
| 12 | WIF | 1540 |
| 13 | Vueling | 1537 |
| 14 | LXJ | 1459 |
| 15 | easyJet | 1276 |
| 16 | Swiss International | 1271 |
| 17 | AXM | 1245 |
| 18 | QLK | 1153 |
| 19 | EJU | 1151 |
| 20 | All Nippon Airways | 1140 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1027 |
| 23 | GLO | 997 |
| 24 | Air France | 966 |
| 25 | AEE | 965 |
| 26 | CXK | 960 |
| 27 | PGT | 955 |
| 28 | United Airlines | 950 |
| 29 | Cathay Pacific | 947 |
| 30 | MXY | 922 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159089 |
| 2 | 🇪🇸 ES | 11950 |
| 3 | 🇧🇷 BR | 10680 |
| 4 | 🇦🇺 AU | 10464 |
| 5 | 🇮🇳 IN | 10197 |
| 6 | 🇨🇦 CA | 10173 |
| 7 | 🇮🇹 IT | 9624 |
| 8 | 🇩🇪 DE | 9187 |
| 9 | 🇬🇧 GB | 8630 |
| 10 | 🇯🇵 JP | 7611 |
| 11 | 🇫🇷 FR | 7431 |
| 12 | 🇨🇴 CO | 7026 |
| 13 | 🇬🇷 GR | 5456 |
| 14 | 🇲🇽 MX | 5320 |
| 15 | 🇨🇭 CH | 4979 |
| 16 | 🇹🇷 TR | 4900 |
| 17 | 🇳🇴 NO | 4786 |
| 18 | 🇲🇾 MY | 3255 |
| 19 | 🇿🇦 ZA | 3126 |
| 20 | 🇵🇱 PL | 3094 |
| 21 | 🇹🇭 TH | 2881 |
| 22 | 🇳🇿 NZ | 2662 |
| 23 | 🇵🇭 PH | 2466 |
| 24 | 🇬🇹 GT | 2375 |
| 25 | 🇰🇷 KR | 2309 |
| 26 | 🇲🇦 MA | 1888 |
| 27 | 🇭🇷 HR | 1878 |
| 28 | 🇲🇪 ME | 1676 |
| 29 | 🇳🇱 NL | 1661 |
| 30 | 🇲🇴 MO | 1522 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3866 |
| 2 | Denver International Airport |  | US | 3069 |
| 3 | Tokyo International Airport |  | JP | 2356 |
| 4 | Indira Gandhi International Airport |  | IN | 2293 |
| 5 | Guaymaral Airport |  | CO | 2273 |
| 6 | Harry Reid International Airport |  | US | 2182 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1990 |
| 8 | Zurich Airport |  | CH | 1984 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1931 |
| 10 | La Aurora Airport |  | GT | 1822 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1672 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1602 |
| 16 | Congonhas Airport |  | BR | 1553 |
| 17 | Macau International Airport |  | MO | 1522 |
| 18 | Madrid Barajas International Airport |  | ES | 1464 |
| 19 | Capua Airport |  | IT | 1458 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1454 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1389 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1330 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1305 |
| 24 | Malpensa International Airport |  | IT | 1284 |
| 25 | Charles de Gaulle International Airport |  | FR | 1270 |
| 26 | Charlotte/Douglas International Airport |  | US | 1256 |
| 27 | Kuala Lumpur International Airport |  | MY | 1219 |
| 28 | Bengaluru International Airport |  | IN | 1205 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1167 |
| 30 | Ninoy Aquino International Airport |  | PH | 1163 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1143 |
| 32 | Barcelona International Airport |  | ES | 1105 |
| 33 | Seattle-Tacoma International Airport |  | US | 1074 |
| 34 | Reno/Tahoe International Airport |  | US | 1073 |
| 35 | Viracopos International Airport |  | BR | 1070 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1038 |
| 39 | Tenerife Norte Airport |  | ES | 1014 |
| 40 | Vitoria/Foronda Airport |  | ES | 1009 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 452 | 1h 7m | 770 km | 6,004.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 313 | 27m | 275 km | 1,483.2 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 302 | 1h 7m | 706 km | 3,676.9 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 279 | 44m | 241 km | 1,158.9 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 266 | 1h 49m | 1,423 km | 6,528.1 t |
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
| HM1 |  | Melbourne Essendon Airport (YMEN) | Melbourne Moorabbin Airport (YMMB) | 2026-08-11 09:03 UTC | 2026-08-11 09:21 UTC | 17m |
| DEOLB | DEO | Kiel-Holtenau Airport (EDHK) | Kiel-Holtenau Airport (EDHK) | 2026-08-11 09:03 UTC | 2026-08-11 09:14 UTC | 11m |
| JUNO76 | JUN | Oakey Airport (YBOK) | Toowoomba Airport (YTWB) | 2026-08-11 08:51 UTC | 2026-08-11 09:13 UTC | 22m |
| HBZPV | HBZ | Ambri Airport (LSPM) | Meiringen Airport (LSMM) | 2026-08-11 08:37 UTC | 2026-08-11 09:10 UTC | 33m |
| KAI | KAI | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-11 08:53 UTC | 2026-08-11 09:10 UTC | 17m |
| THY27D | Turkish Airlines | Istanbul Airport (LTFM) | Istanbul Airport (LTFM) | 2026-08-10 10:19 UTC | 2026-08-11 09:09 UTC | 22h 49m |
| FR142 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-11 09:08 UTC | 2026-08-11 09:08 UTC | 0m |
| OAL040 | OAL | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-08-11 08:18 UTC | 2026-08-11 08:58 UTC | 39m |
| EFC26P | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-11 08:42 UTC | 2026-08-11 08:56 UTC | 13m |
| JAL325 | Japan Airlines | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-11 07:48 UTC | 2026-08-11 08:54 UTC | 1h 6m |
| OCN69 | OCN | Orlando International Airport (KMCO) | Frankfurt am Main International Airport (EDDF) | 2026-08-11 00:20 UTC | 2026-08-11 08:53 UTC | 8h 32m |
| DEOLB | DEO | Kiel-Holtenau Airport (EDHK) | Kiel-Holtenau Airport (EDHK) | 2026-08-11 08:38 UTC | 2026-08-11 08:48 UTC | 10m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Melanes Airport (BIMN) | 2026-08-11 08:14 UTC | 2026-08-11 08:40 UTC | 26m |
| SUI752 | SUI | Dubendorf Airport (LSMD) | Leipzig Halle Airport (EDDP) | 2026-08-11 07:45 UTC | 2026-08-11 08:39 UTC | 53m |
| EFC30K | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-11 08:22 UTC | 2026-08-11 08:34 UTC | 11m |
| TVF46VR | TVF | Paris-Orly Airport (LFPO) | Fes Sefrou Airport (GMFU) | 2026-08-11 06:21 UTC | 2026-08-11 08:33 UTC | 2h 12m |
| HBZZX | HBZ | Gruyeres Airport (LSGT) | Bex Airport (LSGB) | 2026-08-11 07:32 UTC | 2026-08-11 08:29 UTC | 56m |
| WUK276 | WUK | London Luton Airport (EGGW) | Tsalapita Airport (LB11) | 2026-08-11 05:49 UTC | 2026-08-11 08:28 UTC | 2h 38m |
| VOE4ER | VOE | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-11 07:50 UTC | 2026-08-11 08:27 UTC | 37m |
| BNOR | BNO | Mo i Rana Airport Rossvoll (ENRA) | Svolvær Helle Airport (ENSH) | 2026-08-11 07:56 UTC | 2026-08-11 08:27 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
