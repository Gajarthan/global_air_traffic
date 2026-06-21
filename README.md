# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_13:05:16_UTC-green)

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

**Latest saved flight:** 2026-06-21 13:05:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-21 13:05:16 UTC

- **116,165** saved flights
- **40,206** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **116,165** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,412,530.4 tonnes** estimated CO2 emissions
- **81,885,822 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4798 |
| 2 | SkyWest Airlines | 4309 |
| 3 | IndiGo | 2250 |
| 4 | EJA | 2246 |
| 5 | American Airlines | 1813 |
| 6 | Southwest Airlines | 1728 |
| 7 | ENY | 1445 |
| 8 | Delta Air Lines | 1369 |
| 9 | Lufthansa | 1289 |
| 10 | Vueling | 1047 |
| 11 | WIF | 1027 |
| 12 | LATAM Airlines | 1021 |
| 13 | AZU | 967 |
| 14 | AXM | 958 |
| 15 | LXJ | 882 |
| 16 | Swiss International | 820 |
| 17 | All Nippon Airways | 799 |
| 18 | Alaska Airlines | 779 |
| 19 | QLK | 751 |
| 20 | easyJet | 745 |
| 21 | EJU | 729 |
| 22 | Cathay Pacific | 673 |
| 23 | AEE | 653 |
| 24 | VIV | 643 |
| 25 | United Airlines | 642 |
| 26 | Air France | 638 |
| 27 | CXK | 620 |
| 28 | MXY | 614 |
| 29 | AXB | 575 |
| 30 | GLO | 567 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 98004 |
| 2 | 🇪🇸 ES | 7924 |
| 3 | 🇮🇳 IN | 7088 |
| 4 | 🇦🇺 AU | 6884 |
| 5 | 🇧🇷 BR | 6395 |
| 6 | 🇮🇹 IT | 6218 |
| 7 | 🇩🇪 DE | 6200 |
| 8 | 🇨🇦 CA | 6091 |
| 9 | 🇯🇵 JP | 5230 |
| 10 | 🇬🇧 GB | 5073 |
| 11 | 🇫🇷 FR | 4622 |
| 12 | 🇨🇴 CO | 3986 |
| 13 | 🇲🇽 MX | 3418 |
| 14 | 🇬🇷 GR | 3321 |
| 15 | 🇳🇴 NO | 3193 |
| 16 | 🇨🇭 CH | 2976 |
| 17 | 🇲🇾 MY | 2489 |
| 18 | 🇹🇷 TR | 2358 |
| 19 | 🇿🇦 ZA | 1960 |
| 20 | 🇵🇱 PL | 1911 |
| 21 | 🇳🇿 NZ | 1905 |
| 22 | 🇹🇭 TH | 1890 |
| 23 | 🇰🇷 KR | 1889 |
| 24 | 🇵🇭 PH | 1690 |
| 25 | 🇬🇹 GT | 1637 |
| 26 | 🇲🇦 MA | 1264 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1143 |
| 29 | 🇳🇱 NL | 1121 |
| 30 | 🇭🇷 HR | 1014 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2448 |
| 2 | Denver International Airport |  | US | 1954 |
| 3 | Tokyo International Airport |  | JP | 1733 |
| 4 | Indira Gandhi International Airport |  | IN | 1555 |
| 5 | Guaymaral Airport |  | CO | 1476 |
| 6 | Harry Reid International Airport |  | US | 1453 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1422 |
| 8 | Zurich Airport |  | CH | 1296 |
| 9 | La Aurora Airport |  | GT | 1264 |
| 10 | Frankfurt am Main International Airport |  | DE | 1258 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1239 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1156 |
| 15 | Chicago O'Hare International Airport |  | US | 1140 |
| 16 | Capua Airport |  | IT | 1012 |
| 17 | Salt Lake City International Airport |  | US | 996 |
| 18 | Madrid Barajas International Airport |  | ES | 987 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 970 |
| 20 | Kuala Lumpur International Airport |  | MY | 962 |
| 21 | Congonhas Airport |  | BR | 887 |
| 22 | Charlotte/Douglas International Airport |  | US | 887 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 865 |
| 24 | Bengaluru International Airport |  | IN | 858 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 855 |
| 26 | Charles de Gaulle International Airport |  | FR | 854 |
| 27 | Malpensa International Airport |  | IT | 826 |
| 28 | Ninoy Aquino International Airport |  | PH | 780 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 760 |
| 30 | Daniel K Inouye International Airport |  | US | 758 |
| 31 | Tenerife Norte Airport |  | ES | 756 |
| 32 | Barcelona International Airport |  | ES | 741 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 731 |
| 34 | Don Mueang International Airport |  | TH | 685 |
| 35 | Vitoria/Foronda Airport |  | ES | 684 |
| 36 | Calgary International Airport |  | CA | 680 |
| 37 | Amsterdam Airport Schiphol |  | NL | 680 |
| 38 | Seattle-Tacoma International Airport |  | US | 667 |
| 39 | Scottsdale Airport |  | US | 661 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 660 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 612 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 423 | 21m | 244 km | 1,781.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 311 | 24m | 225 km | 1,206.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 299 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 285 | 1h 25m | 910 km | 4,472.3 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 281 | 1h 10m | 770 km | 3,732.9 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 230 | 19m | 165 km | 654.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 217 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 174 | 22m | 55 km | 165.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 20 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 153 | 44m | 241 km | 635.5 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 143 | 1h 44m | 1,423 km | 3,509.4 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 136 | 1h 39m | 1,156 km | 2,713.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 132 | 1h 17m | 961 km | 2,188.0 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N220JG |  | FL47 (FL47) | FL47 (FL47) | 2026-06-21 12:28 UTC | 2026-06-21 13:05 UTC | 36m |
| N8286E |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-06-21 12:24 UTC | 2026-06-21 12:58 UTC | 33m |
| SCA47 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-06-21 12:19 UTC | 2026-06-21 12:54 UTC | 34m |
| N6175Q |  | Lakeland Linder International Airport (KLAL) | Bartow Executive Airport (KBOW) | 2026-06-21 11:59 UTC | 2026-06-21 12:52 UTC | 52m |
| N914PA |  | Merritt Island Airport (KCOI) | Space Coast Regional Airport (KTIX) | 2026-06-21 12:34 UTC | 2026-06-21 12:47 UTC | 12m |
| MABTE | MAB | Bergamo / Orio Al Serio Airport (LIME) | Torino / Caselle International Airport (LIMF) | 2026-06-21 12:21 UTC | 2026-06-21 12:46 UTC | 25m |
| N1168X |  | Linden Airport (KLDJ) | Solberg/Hunterdon Airport (KN51) | 2026-06-21 12:10 UTC | 2026-06-21 12:46 UTC | 36m |
| GCIUW | GCI | White Waltham Airfield (EGLM) | DCAE Cosford Airport (EGWC) | 2026-06-21 11:53 UTC | 2026-06-21 12:41 UTC | 47m |
| AOS50 | AOS | Gloucestershire Airport (EGBJ) | Gloucestershire Airport (EGBJ) | 2026-06-21 10:37 UTC | 2026-06-21 12:39 UTC | 2h 1m |
| ANA868 | All Nippon Airways | Gimpo International Airport (RKSS) | Tokyo International Airport (RJTT) | 2026-06-21 11:03 UTC | 2026-06-21 12:38 UTC | 1h 35m |
| EPI235 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | North Exuma Airport (85FA) | 2026-06-21 12:00 UTC | 2026-06-21 12:38 UTC | 38m |
| N9657G |  | Atlantic City International Airport (KACY) | Wings Field (KLOM) | 2026-06-21 12:10 UTC | 2026-06-21 12:37 UTC | 27m |
| GCMTK | GCM | Bodmin Airfield (EGLA) | Bodmin Airfield (EGLA) | 2026-06-21 12:10 UTC | 2026-06-21 12:35 UTC | 24m |
| HBKNI | HBK | Locarno Airport (LSZL) | Raron Airport (LSTA) | 2026-06-21 12:00 UTC | 2026-06-21 12:34 UTC | 34m |
| RYR59LA | Ryanair | London Stansted Airport (EGSS) | Pruszcz Gdański Airport (EPPR) | 2026-06-21 11:02 UTC | 2026-06-21 12:31 UTC | 1h 29m |
| N7966G |  | Deland Municipal-Sidney H Taylor Field (KDED) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-06-21 12:29 UTC | 2026-06-21 12:30 UTC | 1m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-21 11:59 UTC | 2026-06-21 12:29 UTC | 29m |
| SWR77A | Swiss International | Zurich Airport (LSZH) | Poznań-Ławica Airport (EPPO) | 2026-06-21 11:10 UTC | 2026-06-21 12:28 UTC | 1h 17m |
| CFG6CL | CFG | Munich International Airport (EDDM) | Palma De Mallorca Airport (LEPA) | 2026-06-21 10:38 UTC | 2026-06-21 12:27 UTC | 1h 49m |
| N786FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-06-21 11:34 UTC | 2026-06-21 12:27 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
