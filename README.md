# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_11:11:53_UTC-green)

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

**Latest saved flight:** 2026-08-11 11:11:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 11:11:53 UTC

- **186,438** saved flights
- **59,130** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **186,438** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,237,360.2 tonnes** estimated CO2 emissions
- **129,702,038 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7396 |
| 2 | SkyWest Airlines | 6785 |
| 3 | EJA | 3676 |
| 4 | IndiGo | 3257 |
| 5 | Southwest Airlines | 2925 |
| 6 | American Airlines | 2902 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2193 |
| 9 | LATAM Airlines | 1740 |
| 10 | AZU | 1673 |
| 11 | Lufthansa | 1635 |
| 12 | WIF | 1542 |
| 13 | Vueling | 1537 |
| 14 | LXJ | 1460 |
| 15 | easyJet | 1277 |
| 16 | Swiss International | 1274 |
| 17 | AXM | 1247 |
| 18 | QLK | 1154 |
| 19 | EJU | 1151 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1027 |
| 23 | GLO | 997 |
| 24 | Air France | 969 |
| 25 | AEE | 966 |
| 26 | CXK | 960 |
| 27 | PGT | 956 |
| 28 | United Airlines | 950 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 924 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159094 |
| 2 | 🇪🇸 ES | 11989 |
| 3 | 🇧🇷 BR | 10680 |
| 4 | 🇦🇺 AU | 10479 |
| 5 | 🇮🇳 IN | 10215 |
| 6 | 🇨🇦 CA | 10178 |
| 7 | 🇮🇹 IT | 9644 |
| 8 | 🇩🇪 DE | 9205 |
| 9 | 🇬🇧 GB | 8650 |
| 10 | 🇯🇵 JP | 7640 |
| 11 | 🇫🇷 FR | 7448 |
| 12 | 🇨🇴 CO | 7026 |
| 13 | 🇬🇷 GR | 5469 |
| 14 | 🇲🇽 MX | 5320 |
| 15 | 🇨🇭 CH | 4987 |
| 16 | 🇹🇷 TR | 4904 |
| 17 | 🇳🇴 NO | 4793 |
| 18 | 🇲🇾 MY | 3260 |
| 19 | 🇿🇦 ZA | 3138 |
| 20 | 🇵🇱 PL | 3098 |
| 21 | 🇹🇭 TH | 2884 |
| 22 | 🇳🇿 NZ | 2664 |
| 23 | 🇵🇭 PH | 2469 |
| 24 | 🇬🇹 GT | 2375 |
| 25 | 🇰🇷 KR | 2311 |
| 26 | 🇲🇦 MA | 1892 |
| 27 | 🇭🇷 HR | 1881 |
| 28 | 🇲🇪 ME | 1677 |
| 29 | 🇳🇱 NL | 1663 |
| 30 | 🇲🇴 MO | 1522 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3866 |
| 2 | Denver International Airport |  | US | 3069 |
| 3 | Tokyo International Airport |  | JP | 2363 |
| 4 | Indira Gandhi International Airport |  | IN | 2298 |
| 5 | Guaymaral Airport |  | CO | 2273 |
| 6 | Harry Reid International Airport |  | US | 2182 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1992 |
| 8 | Zurich Airport |  | CH | 1986 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1931 |
| 10 | La Aurora Airport |  | GT | 1822 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1672 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1603 |
| 16 | Congonhas Airport |  | BR | 1553 |
| 17 | Macau International Airport |  | MO | 1522 |
| 18 | Madrid Barajas International Airport |  | ES | 1467 |
| 19 | Capua Airport |  | IT | 1458 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1454 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1389 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1330 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1285 |
| 25 | Charles de Gaulle International Airport |  | FR | 1274 |
| 26 | Charlotte/Douglas International Airport |  | US | 1256 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1205 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1167 |
| 30 | Ninoy Aquino International Airport |  | PH | 1165 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1143 |
| 32 | Barcelona International Airport |  | ES | 1106 |
| 33 | Seattle-Tacoma International Airport |  | US | 1074 |
| 34 | Reno/Tahoe International Airport |  | US | 1073 |
| 35 | Viracopos International Airport |  | BR | 1070 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1040 |
| 39 | Tenerife Norte Airport |  | ES | 1022 |
| 40 | Vitoria/Foronda Airport |  | ES | 1010 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 453 | 1h 7m | 770 km | 6,017.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 329 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 313 | 27m | 275 km | 1,483.2 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 279 | 44m | 241 km | 1,158.9 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 266 | 1h 49m | 1,423 km | 6,528.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 233 | 27m | 215 km | 862.9 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
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
| CAL116 | CAL | Taiwan Taoyuan International Airport (RCTP) | Iki Airport (RJDB) | 2026-08-11 09:14 UTC | 2026-08-11 11:11 UTC | 1h 57m |
| VJT915 | VJT | Luqa Airport (LMML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-11 10:15 UTC | 2026-08-11 11:10 UTC | 55m |
| MSR847 | EgyptAir | HE42 (HE42) | Mohammed V International Airport (GMMN) | 2026-08-11 06:26 UTC | 2026-08-11 11:06 UTC | 4h 39m |
| BRK97 | BRK | Papa Airport (LHPA) | Otocac Airport (LDRO) | 2026-08-11 10:34 UTC | 2026-08-11 11:03 UTC | 28m |
| FDA536 | FDA | Sendai Airport (RJSS) | Ashiya Airport (RJFA) | 2026-08-11 09:21 UTC | 2026-08-11 10:44 UTC | 1h 23m |
| JAL329 | Japan Airlines | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-11 09:32 UTC | 2026-08-11 10:40 UTC | 1h 7m |
| AM280 |  | Newcastle Airport (YWLM) | Walcha Airport (YWCH) | 2026-08-11 10:07 UTC | 2026-08-11 10:39 UTC | 31m |
| JJP984 | JJP | Chitose Air Base (RJCJ) | Ashiya Airport (RJFA) | 2026-08-11 08:40 UTC | 2026-08-11 10:34 UTC | 1h 53m |
| ROT603W | ROT | Henri Coanda International Airport (LROP) | Caransebes Airport (LRCS) | 2026-08-11 10:00 UTC | 2026-08-11 10:27 UTC | 26m |
| ROF9142 | ROF | Campia Turzii Air Base (LRCT) | Timisoara Traian Vuia Airport (LRTR) | 2026-08-11 09:58 UTC | 2026-08-11 10:26 UTC | 27m |
| IGREI | IGR | Cuneo / Levaldigi Airport (LIMZ) | Cuneo / Levaldigi Airport (LIMZ) | 2026-08-11 09:42 UTC | 2026-08-11 10:20 UTC | 38m |
| N211CC |  | Oakland County International Airport (KPTK) | Lakes Of The North Airport (K4Y4) | 2026-08-11 09:51 UTC | 2026-08-11 10:19 UTC | 28m |
| HTT104 | HTT | Buffalo Niagara International Airport (KBUF) | Toronto Pearson International Airport (CYYZ) | 2026-08-11 09:56 UTC | 2026-08-11 10:16 UTC | 19m |
| DTA120 | DTA | Quatro De Fevereiro Airport (FNLU) | Soyo Airport (FNSO) | 2026-08-11 09:38 UTC | 2026-08-11 10:15 UTC | 36m |
| CTV764 | CTV | Soekarno-Hatta International Airport (WIII) | Achmad Yani Airport (WARS) | 2026-08-11 09:38 UTC | 2026-08-11 10:15 UTC | 37m |
| RYR5TA | Ryanair | Valencia Airport (LEVC) | Malpensa International Airport (LIMC) | 2026-08-11 08:36 UTC | 2026-08-11 10:12 UTC | 1h 36m |
| CNF618 | CNF | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-08-11 10:00 UTC | 2026-08-11 10:12 UTC | 11m |
| SEMJG | SEM | Malmo Sturup Airport (ESMS) | Olanda Airport (ESMZ) | 2026-08-11 09:15 UTC | 2026-08-11 10:10 UTC | 55m |
| HBZVQ | HBZ | Muenster Aero Airport (LSPU) | Meiringen Airport (LSMM) | 2026-08-11 09:19 UTC | 2026-08-11 10:07 UTC | 47m |
| JFA96W | JFA | Sofia Airport (LBSF) | Samedan Airport (LSZS) | 2026-08-11 08:11 UTC | 2026-08-11 10:07 UTC | 1h 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
