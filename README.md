# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_13:18:54_UTC-green)

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

**Latest saved flight:** 2026-08-03 13:18:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 13:18:54 UTC

- **168,522** saved flights
- **55,045** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **168,522** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **2,032,252.6 tonnes** estimated CO2 emissions
- **117,811,746 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6723 |
| 2 | SkyWest Airlines | 6146 |
| 3 | EJA | 3349 |
| 4 | IndiGo | 2975 |
| 5 | American Airlines | 2657 |
| 6 | Southwest Airlines | 2652 |
| 7 | ENY | 2099 |
| 8 | Delta Air Lines | 2010 |
| 9 | LATAM Airlines | 1564 |
| 10 | Lufthansa | 1550 |
| 11 | AZU | 1483 |
| 12 | WIF | 1409 |
| 13 | Vueling | 1388 |
| 14 | LXJ | 1318 |
| 15 | AXM | 1166 |
| 16 | Swiss International | 1154 |
| 17 | easyJet | 1136 |
| 18 | EJU | 1036 |
| 19 | Alaska Airlines | 1031 |
| 20 | QLK | 1028 |
| 21 | All Nippon Airways | 1023 |
| 22 | VIV | 929 |
| 23 | Cathay Pacific | 901 |
| 24 | CXK | 893 |
| 25 | United Airlines | 889 |
| 26 | AEE | 882 |
| 27 | GLO | 882 |
| 28 | Air France | 871 |
| 29 | MXY | 864 |
| 30 | JetBlue | 850 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145186 |
| 2 | 🇪🇸 ES | 10804 |
| 3 | 🇧🇷 BR | 9589 |
| 4 | 🇦🇺 AU | 9409 |
| 5 | 🇮🇳 IN | 9316 |
| 6 | 🇨🇦 CA | 9125 |
| 7 | 🇮🇹 IT | 8702 |
| 8 | 🇩🇪 DE | 8413 |
| 9 | 🇬🇧 GB | 7842 |
| 10 | 🇯🇵 JP | 6788 |
| 11 | 🇫🇷 FR | 6687 |
| 12 | 🇨🇴 CO | 6079 |
| 13 | 🇬🇷 GR | 4895 |
| 14 | 🇲🇽 MX | 4817 |
| 15 | 🇨🇭 CH | 4443 |
| 16 | 🇳🇴 NO | 4403 |
| 17 | 🇹🇷 TR | 4084 |
| 18 | 🇲🇾 MY | 3035 |
| 19 | 🇵🇱 PL | 2843 |
| 20 | 🇿🇦 ZA | 2743 |
| 21 | 🇹🇭 TH | 2453 |
| 22 | 🇳🇿 NZ | 2448 |
| 23 | 🇵🇭 PH | 2235 |
| 24 | 🇬🇹 GT | 2182 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1706 |
| 27 | 🇭🇷 HR | 1618 |
| 28 | 🇲🇪 ME | 1560 |
| 29 | 🇳🇱 NL | 1539 |
| 30 | 🇲🇴 MO | 1433 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3457 |
| 2 | Denver International Airport |  | US | 2799 |
| 3 | Tokyo International Airport |  | JP | 2132 |
| 4 | Guaymaral Airport |  | CO | 2099 |
| 5 | Indira Gandhi International Airport |  | IN | 2065 |
| 6 | Harry Reid International Airport |  | US | 2027 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1845 |
| 8 | Zurich Airport |  | CH | 1791 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1772 |
| 10 | La Aurora Airport |  | GT | 1684 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1554 |
| 12 | El Dorado International Airport |  | CO | 1526 |
| 13 | Chicago O'Hare International Airport |  | US | 1525 |
| 14 | Frankfurt am Main International Airport |  | DE | 1514 |
| 15 | Salt Lake City International Airport |  | US | 1506 |
| 16 | Macau International Airport |  | MO | 1433 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1394 |
| 18 | Congonhas Airport |  | BR | 1380 |
| 19 | Madrid Barajas International Airport |  | ES | 1328 |
| 20 | Capua Airport |  | IT | 1312 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1279 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1191 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1184 |
| 24 | Charlotte/Douglas International Airport |  | US | 1172 |
| 25 | Charles de Gaulle International Airport |  | FR | 1150 |
| 26 | Kuala Lumpur International Airport |  | MY | 1144 |
| 27 | Malpensa International Airport |  | IT | 1135 |
| 28 | Bengaluru International Airport |  | IN | 1105 |
| 29 | Ninoy Aquino International Airport |  | PH | 1051 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1039 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1035 |
| 32 | Barcelona International Airport |  | ES | 999 |
| 33 | Daniel K Inouye International Airport |  | US | 981 |
| 34 | Seattle-Tacoma International Airport |  | US | 978 |
| 35 | Viracopos International Airport |  | BR | 961 |
| 36 | Calgary International Airport |  | CA | 952 |
| 37 | Tenerife Norte Airport |  | ES | 939 |
| 38 | Reno/Tahoe International Airport |  | US | 936 |
| 39 | Oslo Gardermoen Airport |  | NO | 936 |
| 40 | Scottsdale Airport |  | US | 932 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 872 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 614 | 21m | 244 km | 2,585.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 403 | 24m | 225 km | 1,563.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 402 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 289 | 27m | 275 km | 1,369.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 247 | 44m | 241 km | 1,026.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 232 | 1h 47m | 1,423 km | 5,693.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 200 | 19m | 144 km | 497.5 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 196 | 50m | 556 km | 1,878.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 189 | 1h 38m | 1,156 km | 3,770.5 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 185 | 24m | 218 km | 697.0 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBKLA | HBK | Lommis Airfield (LSZT) | Friedrichshafen Airport (EDNY) | 2026-08-03 12:53 UTC | 2026-08-03 13:18 UTC | 25m |
| N62650 |  | Punta Gorda Airport (KPGD) | Miami Executive Airport (KTMB) | 2026-08-03 12:23 UTC | 2026-08-03 13:13 UTC | 50m |
| SHADY09 | SHA | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-08-03 12:52 UTC | 2026-08-03 13:07 UTC | 15m |
| CXK557 | CXK | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-03 12:45 UTC | 2026-08-03 13:03 UTC | 18m |
| DIFLE | DIF | Harle Airport (EDXP) | Wangerooge Airport (EDWG) | 2026-08-03 12:58 UTC | 2026-08-03 13:02 UTC | 3m |
| N193RA |  | Laredo International Airport (KLRD) | Brownsville/South Padre Island International Airport (KBRO) | 2026-08-03 12:10 UTC | 2026-08-03 12:56 UTC | 45m |
| ROKT21 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Sky Landings Airport (22MS) | 2026-08-03 12:34 UTC | 2026-08-03 12:55 UTC | 20m |
| D0381 |  | Schwabach-Heidenberg Airport (EDPH) | Schwabach-Heidenberg Airport (EDPH) | 2026-08-03 11:59 UTC | 2026-08-03 12:55 UTC | 55m |
| N351WT |  | Lincoln Airport (KLNK) | Loup City Municipal Airport (K0F4) | 2026-08-03 12:21 UTC | 2026-08-03 12:54 UTC | 32m |
| N87FP |  | Spirit Of St Louis Airport (KSUS) | Antrim County Airport (KACB) | 2026-08-03 11:05 UTC | 2026-08-03 12:53 UTC | 1h 47m |
| N20AW |  | Republic Airport (KFRG) | Laguardia Airport (KLGA) | 2026-08-03 12:26 UTC | 2026-08-03 12:50 UTC | 24m |
| HAKAR | HAK | Belgrade Nikola Tesla Airport (LYBE) | Otocac Airport (LDRO) | 2026-08-03 12:03 UTC | 2026-08-03 12:50 UTC | 46m |
| SXS78U | SXS | Memmingen Allgau Airport (EDJA) | Karain Airport (LTXE) | 2026-08-03 10:12 UTC | 2026-08-03 12:50 UTC | 2h 38m |
| WIF69D | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-03 12:12 UTC | 2026-08-03 12:50 UTC | 37m |
| N963JA |  | Deland Municipal-Sidney H Taylor Field (KDED) | North Exuma Airport (85FA) | 2026-08-03 12:36 UTC | 2026-08-03 12:49 UTC | 13m |
| FCTMS | FCT | Chateau-Arnoux-Saint-Auban Airport (LFMX) | Barcelonnette - Saint-Pons Airport (LFMR) | 2026-08-03 12:15 UTC | 2026-08-03 12:49 UTC | 34m |
| MILLER2 | MIL | Roger M Dreyer Memorial Airport (KT20) | Roger M Dreyer Memorial Airport (KT20) | 2026-08-03 12:38 UTC | 2026-08-03 12:49 UTC | 11m |
| N316TT |  | Mineral Wells Regional Airport (KMWL) | 2XA0 (2XA0) | 2026-08-03 12:19 UTC | 2026-08-03 12:49 UTC | 29m |
| 8QTAN |  | Dharavandhoo Airport (VRMD) | Dharavandhoo Airport (VRMD) | 2026-08-03 12:45 UTC | 2026-08-03 12:46 UTC | 1m |
| SXHRE | SXH | Paros Airport (LGPA) | Eleftherios Venizelos International Airport (LGAV) | 2026-08-03 12:06 UTC | 2026-08-03 12:46 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
