# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_17:52:11_UTC-green)

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

**Latest saved flight:** 2026-07-13 17:52:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-13 17:52:11 UTC

- **140,387** saved flights
- **47,234** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **140,387** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,685,454.7 tonnes** estimated CO2 emissions
- **97,707,517 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5719 |
| 2 | SkyWest Airlines | 5137 |
| 3 | EJA | 2764 |
| 4 | IndiGo | 2576 |
| 5 | American Airlines | 2220 |
| 6 | Southwest Airlines | 2113 |
| 7 | ENY | 1747 |
| 8 | Delta Air Lines | 1665 |
| 9 | Lufthansa | 1427 |
| 10 | LATAM Airlines | 1290 |
| 11 | Vueling | 1213 |
| 12 | WIF | 1208 |
| 13 | AZU | 1207 |
| 14 | LXJ | 1074 |
| 15 | AXM | 1048 |
| 16 | Swiss International | 1004 |
| 17 | easyJet | 917 |
| 18 | All Nippon Airways | 899 |
| 19 | Alaska Airlines | 881 |
| 20 | QLK | 877 |
| 21 | EJU | 865 |
| 22 | VIV | 774 |
| 23 | AEE | 754 |
| 24 | Air France | 753 |
| 25 | CXK | 752 |
| 26 | JetBlue | 741 |
| 27 | United Airlines | 733 |
| 28 | Cathay Pacific | 729 |
| 29 | MXY | 728 |
| 30 | GLO | 719 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 120581 |
| 2 | 🇪🇸 ES | 9215 |
| 3 | 🇮🇳 IN | 8067 |
| 4 | 🇦🇺 AU | 8018 |
| 5 | 🇧🇷 BR | 7926 |
| 6 | 🇨🇦 CA | 7356 |
| 7 | 🇮🇹 IT | 7331 |
| 8 | 🇩🇪 DE | 7324 |
| 9 | 🇬🇧 GB | 6407 |
| 10 | 🇯🇵 JP | 5895 |
| 11 | 🇫🇷 FR | 5600 |
| 12 | 🇨🇴 CO | 4447 |
| 13 | 🇲🇽 MX | 4071 |
| 14 | 🇬🇷 GR | 4000 |
| 15 | 🇳🇴 NO | 3782 |
| 16 | 🇨🇭 CH | 3653 |
| 17 | 🇹🇷 TR | 3311 |
| 18 | 🇲🇾 MY | 2731 |
| 19 | 🇵🇱 PL | 2353 |
| 20 | 🇿🇦 ZA | 2304 |
| 21 | 🇳🇿 NZ | 2144 |
| 22 | 🇹🇭 TH | 2110 |
| 23 | 🇰🇷 KR | 2013 |
| 24 | 🇵🇭 PH | 1906 |
| 25 | 🇬🇹 GT | 1857 |
| 26 | 🇲🇦 MA | 1473 |
| 27 | 🇲🇪 ME | 1397 |
| 28 | 🇳🇱 NL | 1325 |
| 29 | 🇭🇷 HR | 1272 |
| 30 | 🇲🇴 MO | 1190 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2894 |
| 2 | Denver International Airport |  | US | 2345 |
| 3 | Tokyo International Airport |  | JP | 1909 |
| 4 | Indira Gandhi International Airport |  | IN | 1787 |
| 5 | Harry Reid International Airport |  | US | 1749 |
| 6 | Guaymaral Airport |  | CO | 1712 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1615 |
| 8 | Zurich Airport |  | CH | 1568 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1475 |
| 10 | La Aurora Airport |  | GT | 1435 |
| 11 | Frankfurt am Main International Airport |  | DE | 1378 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1337 |
| 13 | Chicago O'Hare International Airport |  | US | 1319 |
| 14 | Salt Lake City International Airport |  | US | 1252 |
| 15 | El Dorado International Airport |  | CO | 1244 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1207 |
| 17 | Macau International Airport |  | MO | 1190 |
| 18 | Capua Airport |  | IT | 1149 |
| 19 | Madrid Barajas International Airport |  | ES | 1141 |
| 20 | Congonhas Airport |  | BR | 1130 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1124 |
| 22 | Kuala Lumpur International Airport |  | MY | 1057 |
| 23 | Charlotte/Douglas International Airport |  | US | 1022 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1011 |
| 25 | Charles de Gaulle International Airport |  | FR | 996 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 975 |
| 27 | Bengaluru International Airport |  | IN | 966 |
| 28 | Malpensa International Airport |  | IT | 912 |
| 29 | Ninoy Aquino International Airport |  | PH | 889 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 858 |
| 31 | Daniel K Inouye International Airport |  | US | 857 |
| 32 | Barcelona International Airport |  | ES | 857 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 824 |
| 34 | Tenerife Norte Airport |  | ES | 818 |
| 35 | Calgary International Airport |  | CA | 804 |
| 36 | Viracopos International Airport |  | BR | 799 |
| 37 | Seattle-Tacoma International Airport |  | US | 798 |
| 38 | Amsterdam Airport Schiphol |  | NL | 798 |
| 39 | Scottsdale Airport |  | US | 796 |
| 40 | Vitoria/Foronda Airport |  | ES | 780 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 722 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 507 | 21m | 244 km | 2,134.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 344 | 24m | 225 km | 1,334.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 343 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 333 | 1h 9m | 770 km | 4,423.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 188 | 1h 46m | 1,423 km | 4,613.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 188 | 20m | 99 km | 322.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 185 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 170 | 31m | 369 km | 1,082.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 169 | 18m | 144 km | 420.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 160 | 1h 38m | 1,156 km | 3,191.9 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 154 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LIFELN1 | LIF | 0CO8 (0CO8) | Northern Colorado Regional Airport (KFNL) | 2026-07-13 17:29 UTC | 2026-07-13 17:52 UTC | 22m |
| N805AZ |  | Zamperini Field (KTOA) | Brackett Field (KPOC) | 2026-07-13 17:20 UTC | 2026-07-13 17:49 UTC | 29m |
| TKR107 | TKR | Downey/Hyde Memorial/ Airport (KU58) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-07-13 17:18 UTC | 2026-07-13 17:47 UTC | 29m |
| BURNY40 | BUR | Dave Eby Field (4XA5) | Mc Neill Ranch Airport (6TE7) | 2026-07-13 17:25 UTC | 2026-07-13 17:46 UTC | 20m |
| KSF18 | KSF | Kent State University Airport (K1G3) | Portage County Airport (KPOV) | 2026-07-13 17:23 UTC | 2026-07-13 17:43 UTC | 20m |
| N622TP |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-07-13 17:11 UTC | 2026-07-13 17:41 UTC | 29m |
| XBAEB | XBA | Hermanos Serdan International Airport (MMPB) | General Mariano Matamoros Airport (MMCB) | 2026-07-13 16:39 UTC | 2026-07-13 17:38 UTC | 58m |
| N764DG |  | Salt Lake City International Airport (KSLC) | Provo Municipal Airport (KPVU) | 2026-07-13 16:54 UTC | 2026-07-13 17:38 UTC | 43m |
| ZKICU | ZKI | Wellington International Airport (NZWN) | Wellington International Airport (NZWN) | 2026-07-13 17:17 UTC | 2026-07-13 17:34 UTC | 16m |
| N33NE |  | Ted Stevens Anchorage International Airport (PANC) | King Salmon Airport (PAKN) | 2026-07-13 16:07 UTC | 2026-07-13 17:34 UTC | 1h 26m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-13 16:58 UTC | 2026-07-13 17:33 UTC | 35m |
| UAL17 | United Airlines | London Heathrow Airport (EGLL) | Newark Liberty International Airport (KEWR) | 2026-07-13 10:25 UTC | 2026-07-13 17:32 UTC | 7h 6m |
| N500GP |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-07-13 17:02 UTC | 2026-07-13 17:32 UTC | 29m |
| N3ZZ |  | Bellefontaine Regional Airport (KEDJ) | Bellefontaine Regional Airport (KEDJ) | 2026-07-13 17:19 UTC | 2026-07-13 17:31 UTC | 11m |
| N60143 |  | Santa Ynez/Kunkle Field (KIZA) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-07-13 15:57 UTC | 2026-07-13 17:29 UTC | 1h 32m |
| EAF176 | EAF | Debrecen International Airport (LHDC) | LRPV (LRPV) | 2026-07-13 16:54 UTC | 2026-07-13 17:27 UTC | 32m |
| I2331 |  | Pratica Di Mare Airport (LIRE) | Tivat Airport (LYTV) | 2026-07-13 15:29 UTC | 2026-07-13 17:24 UTC | 1h 54m |
| BLZR258 | BLZ | Kingsville Nas Airport (KNQI) | El Coyote Ranch Airport (2TA8) | 2026-07-13 17:13 UTC | 2026-07-13 17:24 UTC | 11m |
| N606LB |  | Centralia Municipal Airport (KENL) | Centralia Municipal Airport (KENL) | 2026-07-13 17:07 UTC | 2026-07-13 17:23 UTC | 16m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-07-13 17:08 UTC | 2026-07-13 17:22 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
