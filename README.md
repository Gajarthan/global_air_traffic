# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_12:09:44_UTC-green)

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

**Latest saved flight:** 2026-08-11 12:09:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 12:09:44 UTC

- **186,532** saved flights
- **59,153** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **186,532** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,238,894.0 tonnes** estimated CO2 emissions
- **129,790,956 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7402 |
| 2 | SkyWest Airlines | 6785 |
| 3 | EJA | 3676 |
| 4 | IndiGo | 3259 |
| 5 | Southwest Airlines | 2925 |
| 6 | American Airlines | 2902 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2193 |
| 9 | LATAM Airlines | 1741 |
| 10 | AZU | 1674 |
| 11 | Lufthansa | 1636 |
| 12 | WIF | 1543 |
| 13 | Vueling | 1538 |
| 14 | LXJ | 1460 |
| 15 | easyJet | 1280 |
| 16 | Swiss International | 1274 |
| 17 | AXM | 1247 |
| 18 | QLK | 1154 |
| 19 | EJU | 1153 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1027 |
| 23 | GLO | 998 |
| 24 | Air France | 969 |
| 25 | AEE | 966 |
| 26 | CXK | 960 |
| 27 | PGT | 957 |
| 28 | United Airlines | 951 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 924 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159113 |
| 2 | 🇪🇸 ES | 12003 |
| 3 | 🇧🇷 BR | 10686 |
| 4 | 🇦🇺 AU | 10481 |
| 5 | 🇮🇳 IN | 10219 |
| 6 | 🇨🇦 CA | 10180 |
| 7 | 🇮🇹 IT | 9653 |
| 8 | 🇩🇪 DE | 9212 |
| 9 | 🇬🇧 GB | 8670 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7454 |
| 12 | 🇨🇴 CO | 7032 |
| 13 | 🇬🇷 GR | 5473 |
| 14 | 🇲🇽 MX | 5321 |
| 15 | 🇨🇭 CH | 5000 |
| 16 | 🇹🇷 TR | 4911 |
| 17 | 🇳🇴 NO | 4797 |
| 18 | 🇲🇾 MY | 3262 |
| 19 | 🇿🇦 ZA | 3138 |
| 20 | 🇵🇱 PL | 3100 |
| 21 | 🇹🇭 TH | 2885 |
| 22 | 🇳🇿 NZ | 2664 |
| 23 | 🇵🇭 PH | 2471 |
| 24 | 🇬🇹 GT | 2375 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1897 |
| 27 | 🇭🇷 HR | 1887 |
| 28 | 🇲🇪 ME | 1677 |
| 29 | 🇳🇱 NL | 1663 |
| 30 | 🇲🇴 MO | 1522 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3866 |
| 2 | Denver International Airport |  | US | 3069 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2299 |
| 5 | Guaymaral Airport |  | CO | 2277 |
| 6 | Harry Reid International Airport |  | US | 2186 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1992 |
| 8 | Zurich Airport |  | CH | 1986 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1931 |
| 10 | La Aurora Airport |  | GT | 1822 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1672 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1604 |
| 16 | Congonhas Airport |  | BR | 1555 |
| 17 | Macau International Airport |  | MO | 1522 |
| 18 | Madrid Barajas International Airport |  | ES | 1470 |
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
| 30 | Ninoy Aquino International Airport |  | PH | 1166 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1143 |
| 32 | Barcelona International Airport |  | ES | 1107 |
| 33 | Seattle-Tacoma International Airport |  | US | 1074 |
| 34 | Reno/Tahoe International Airport |  | US | 1073 |
| 35 | Viracopos International Airport |  | BR | 1071 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1042 |
| 39 | Tenerife Norte Airport |  | ES | 1023 |
| 40 | Vitoria/Foronda Airport |  | ES | 1011 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 938 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
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
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| T340 |  | Alpnach Air Base (LSMA) | Alpnach Air Base (LSMA) | 2026-08-11 11:58 UTC | 2026-08-11 12:09 UTC | 11m |
| N607PT |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-08-11 11:40 UTC | 2026-08-11 12:06 UTC | 26m |
| GJENK | GJE | Old Warden Airfield (EGTH) | RAF Wyton (EGUY) | 2026-08-11 11:27 UTC | 2026-08-11 12:06 UTC | 39m |
| TUTOR862 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-11 11:50 UTC | 2026-08-11 12:00 UTC | 10m |
| GBZBS | GBZ | White Waltham Airfield (EGLM) | White Waltham Airfield (EGLM) | 2026-08-11 11:40 UTC | 2026-08-11 11:59 UTC | 18m |
| DIMMM | DIM | Hamburg Airport (EDDH) | Wyk auf Fohr Airport (EDXY) | 2026-08-11 11:13 UTC | 2026-08-11 11:57 UTC | 44m |
| WZZ701 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Pecs-Pogany Airport (LHPP) | 2026-08-11 11:29 UTC | 2026-08-11 11:57 UTC | 27m |
| N713SQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-11 11:46 UTC | 2026-08-11 11:56 UTC | 10m |
| CES218 | China Eastern | Geneva Cointrin International Airport (LSGG) | Bornholm Airport (EKRN) | 2026-08-11 10:11 UTC | 2026-08-11 11:45 UTC | 1h 33m |
| OEFDE | OEF | Maribor Airport (LJMB) | Maribor Airport (LJMB) | 2026-08-11 10:02 UTC | 2026-08-11 11:42 UTC | 1h 40m |
| NJE979C | NJE | Helsinki Vantaa Airport (EFHK) | Cannes-Mandelieu Airport (LFMD) | 2026-08-11 08:12 UTC | 2026-08-11 11:41 UTC | 3h 29m |
| THY6929 | Turkish Airlines | Istanbul Airport (LTFM) | Bezymyanka Airfield (UWWG) | 2026-08-11 08:29 UTC | 2026-08-11 11:39 UTC | 3h 10m |
| ANE1281 | ANE | Madrid Barajas International Airport (LEMD) | Belley - Peyrieu Airport (LFKY) | 2026-08-11 09:56 UTC | 2026-08-11 11:36 UTC | 1h 40m |
| JANET33 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-11 11:21 UTC | 2026-08-11 11:34 UTC | 13m |
| OKPID | OKP | Hradec Kralove Airport (LKHK) | Horice Airport (LKHC) | 2026-08-11 11:16 UTC | 2026-08-11 11:33 UTC | 16m |
| A6SSM |  | Fujairah International Airport (OMFJ) | Fujairah International Airport (OMFJ) | 2026-08-11 11:32 UTC | 2026-08-11 11:33 UTC | 0m |
| HK5019G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-11 11:29 UTC | 2026-08-11 11:33 UTC | 4m |
| N104CX |  | Felts Field (KSFF) | MT88 (MT88) | 2026-08-11 11:09 UTC | 2026-08-11 11:32 UTC | 23m |
| UAE256 | Emirates | Licenciado Benito Juarez International Airport (MMMX) | Barcelona International Airport (LEBL) | 2026-08-11 01:09 UTC | 2026-08-11 11:32 UTC | 10h 22m |
| RYR716A | Ryanair | Edinburgh Airport (EGPH) | Vienna International Airport (LOWW) | 2026-08-11 09:18 UTC | 2026-08-11 11:31 UTC | 2h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
