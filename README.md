# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_20:08:42_UTC-green)

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

**Latest saved flight:** 2026-08-12 20:08:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 20:08:42 UTC

- **190,605** saved flights
- **60,166** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **190,605** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,281,568.1 tonnes** estimated CO2 emissions
- **132,264,815 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7560 |
| 2 | SkyWest Airlines | 6903 |
| 3 | EJA | 3762 |
| 4 | IndiGo | 3309 |
| 5 | Southwest Airlines | 2977 |
| 6 | American Airlines | 2957 |
| 7 | ENY | 2360 |
| 8 | Delta Air Lines | 2239 |
| 9 | LATAM Airlines | 1787 |
| 10 | AZU | 1721 |
| 11 | Lufthansa | 1659 |
| 12 | WIF | 1584 |
| 13 | Vueling | 1582 |
| 14 | LXJ | 1494 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1253 |
| 18 | EJU | 1178 |
| 19 | QLK | 1168 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1135 |
| 22 | VIV | 1051 |
| 23 | GLO | 1029 |
| 24 | Air France | 994 |
| 25 | PGT | 985 |
| 26 | CXK | 977 |
| 27 | AEE | 975 |
| 28 | United Airlines | 975 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 947 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 162460 |
| 2 | 🇪🇸 ES | 12294 |
| 3 | 🇧🇷 BR | 10965 |
| 4 | 🇦🇺 AU | 10660 |
| 5 | 🇨🇦 CA | 10440 |
| 6 | 🇮🇳 IN | 10368 |
| 7 | 🇮🇹 IT | 9896 |
| 8 | 🇩🇪 DE | 9423 |
| 9 | 🇬🇧 GB | 8887 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7629 |
| 12 | 🇨🇴 CO | 7325 |
| 13 | 🇬🇷 GR | 5577 |
| 14 | 🇲🇽 MX | 5406 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5084 |
| 17 | 🇳🇴 NO | 4911 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3211 |
| 20 | 🇵🇱 PL | 3152 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2510 |
| 24 | 🇬🇹 GT | 2410 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1957 |
| 27 | 🇲🇦 MA | 1930 |
| 28 | 🇳🇱 NL | 1702 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3954 |
| 2 | Denver International Airport |  | US | 3130 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2357 |
| 5 | Indira Gandhi International Airport |  | IN | 2336 |
| 6 | Harry Reid International Airport |  | US | 2224 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2017 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1975 |
| 10 | La Aurora Airport |  | GT | 1853 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1725 |
| 12 | El Dorado International Airport |  | CO | 1720 |
| 13 | Salt Lake City International Airport |  | US | 1693 |
| 14 | Chicago O'Hare International Airport |  | US | 1666 |
| 15 | Frankfurt am Main International Airport |  | DE | 1626 |
| 16 | Congonhas Airport |  | BR | 1594 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | Capua Airport |  | IT | 1479 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1477 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1406 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1368 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1324 |
| 24 | Malpensa International Airport |  | IT | 1316 |
| 25 | Charles de Gaulle International Airport |  | FR | 1305 |
| 26 | Charlotte/Douglas International Airport |  | US | 1275 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1224 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1192 |
| 30 | Ninoy Aquino International Airport |  | PH | 1186 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1169 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1107 |
| 34 | Reno/Tahoe International Airport |  | US | 1097 |
| 35 | Seattle-Tacoma International Airport |  | US | 1095 |
| 36 | Calgary International Airport |  | CA | 1087 |
| 37 | Daniel K Inouye International Airport |  | US | 1070 |
| 38 | Oslo Gardermoen Airport |  | NO | 1067 |
| 39 | Tenerife Norte Airport |  | ES | 1045 |
| 40 | Vitoria/Foronda Airport |  | ES | 1035 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 974 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 698 | 21m | 244 km | 2,939.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 443 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 321 | 27m | 275 km | 1,521.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 301 | 8m | - | - |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 284 | 44m | 241 km | 1,179.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 274 | 1h 49m | 1,423 km | 6,724.4 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 239 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 231 | 1h 15m | 961 km | 3,828.9 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 228 | 24m | 218 km | 859.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 227 | 19m | 144 km | 564.7 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N682MA |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-12 19:10 UTC | 2026-08-12 20:08 UTC | 58m |
| N58AY |  | Oakland County International Airport (KPTK) | Monmouth Executive Airport (KBLM) | 2026-08-12 18:15 UTC | 2026-08-12 20:04 UTC | 1h 49m |
| TKR15 | TKR | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-08-12 19:43 UTC | 2026-08-12 20:00 UTC | 17m |
| N81CR |  | Perot Field/Fort Worth Alliance Airport (KAFW) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-12 18:09 UTC | 2026-08-12 20:00 UTC | 1h 51m |
| N9546Q |  | Monmouth Executive Airport (KBLM) | Lancaster Airport (KLNS) | 2026-08-12 19:19 UTC | 2026-08-12 19:57 UTC | 38m |
| N27DD |  | William P Hobby Airport (KHOU) | Valley Of The Moon Airport (MS59) | 2026-08-12 18:58 UTC | 2026-08-12 19:57 UTC | 58m |
| N888YW |  | San Gabriel Valley Airport (KEMT) | Riverside Airport (KRAL) | 2026-08-12 18:54 UTC | 2026-08-12 19:54 UTC | 59m |
| N279J |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-12 18:50 UTC | 2026-08-12 19:49 UTC | 58m |
| N65716 |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-12 19:20 UTC | 2026-08-12 19:48 UTC | 28m |
| 217002 |  | Ancient Valley/Pontious Airport (1CL2) | Edwards Af Aux North Base Airport (K9L2) | 2026-08-12 19:26 UTC | 2026-08-12 19:46 UTC | 20m |
| PTN14P | PTN | Manchester Airport (EGCC) | Leeds Bradford Airport (EGNM) | 2026-08-12 19:29 UTC | 2026-08-12 19:45 UTC | 16m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-12 19:08 UTC | 2026-08-12 19:44 UTC | 36m |
| N166RD |  | Pella Municipal Airport (KPEA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-12 18:54 UTC | 2026-08-12 19:39 UTC | 44m |
| N777ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-12 18:31 UTC | 2026-08-12 19:38 UTC | 1h 7m |
| SRG336 | SRG | Caernarfon Airport (EGCK) | Warton Airport (EGNO) | 2026-08-12 19:02 UTC | 2026-08-12 19:37 UTC | 35m |
| N484LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-12 17:22 UTC | 2026-08-12 19:34 UTC | 2h 12m |
| N61AP |  | Van Nuys Airport (KVNY) | Truckee-Tahoe Airport (KTRK) | 2026-08-12 18:10 UTC | 2026-08-12 19:34 UTC | 1h 23m |
| EXS8T | EXS | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-12 18:38 UTC | 2026-08-12 19:33 UTC | 55m |
| CXK444 | CXK | Hartford-Brainard Airport (KHFD) | Hartford-Brainard Airport (KHFD) | 2026-08-12 19:15 UTC | 2026-08-12 19:33 UTC | 17m |
| SVL32 | SVL | Santa Fe Regional Airport (KSAF) | Flagstaff Pulliam Airport (KFLG) | 2026-08-12 18:52 UTC | 2026-08-12 19:33 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
