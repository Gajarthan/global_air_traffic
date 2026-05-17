# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_12:26:51_UTC-green)

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

**Latest saved flight:** 2026-05-17 12:26:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 12:26:51 UTC

- **85,924** saved flights
- **30,796** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,924** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,063,152.3 tonnes** estimated CO2 emissions
- **61,632,018 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3679 |
| 2 | SkyWest Airlines | 3172 |
| 3 | IndiGo | 1857 |
| 4 | EJA | 1612 |
| 5 | American Airlines | 1318 |
| 6 | Southwest Airlines | 1246 |
| 7 | Lufthansa | 1090 |
| 8 | ENY | 1063 |
| 9 | Delta Air Lines | 936 |
| 10 | Vueling | 815 |
| 11 | AXM | 782 |
| 12 | LATAM Airlines | 778 |
| 13 | WIF | 734 |
| 14 | AZU | 672 |
| 15 | All Nippon Airways | 666 |
| 16 | Swiss International | 666 |
| 17 | LXJ | 628 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 611 |
| 20 | easyJet | 569 |
| 21 | Cathay Pacific | 548 |
| 22 | EJU | 546 |
| 23 | AEE | 539 |
| 24 | VIV | 515 |
| 25 | Air France | 503 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 453 |
| 28 | AXB | 452 |
| 29 | MXY | 428 |
| 30 | AIQ | 425 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70240 |
| 2 | 🇪🇸 ES | 6078 |
| 3 | 🇮🇳 IN | 5804 |
| 4 | 🇦🇺 AU | 5473 |
| 5 | 🇩🇪 DE | 4794 |
| 6 | 🇮🇹 IT | 4738 |
| 7 | 🇧🇷 BR | 4718 |
| 8 | 🇯🇵 JP | 4320 |
| 9 | 🇨🇦 CA | 4260 |
| 10 | 🇬🇧 GB | 3671 |
| 11 | 🇫🇷 FR | 3422 |
| 12 | 🇨🇴 CO | 2880 |
| 13 | 🇲🇽 MX | 2642 |
| 14 | 🇬🇷 GR | 2495 |
| 15 | 🇳🇴 NO | 2377 |
| 16 | 🇨🇭 CH | 2280 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1613 |
| 19 | 🇹🇷 TR | 1548 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1501 |
| 22 | 🇵🇱 PL | 1427 |
| 23 | 🇵🇭 PH | 1352 |
| 24 | 🇰🇷 KR | 1352 |
| 25 | 🇬🇹 GT | 1290 |
| 26 | 🇲🇴 MO | 1005 |
| 27 | 🇲🇦 MA | 999 |
| 28 | 🇲🇪 ME | 898 |
| 29 | 🇳🇱 NL | 878 |
| 30 | 🇭🇷 HR | 769 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1874 |
| 2 | Tokyo International Airport |  | JP | 1443 |
| 3 | Denver International Airport |  | US | 1442 |
| 4 | Indira Gandhi International Airport |  | IN | 1245 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1195 |
| 6 | Frankfurt am Main International Airport |  | DE | 1102 |
| 7 | Harry Reid International Airport |  | US | 1088 |
| 8 | Zurich Airport |  | CH | 1024 |
| 9 | Macau International Airport |  | MO | 1005 |
| 10 | La Aurora Airport |  | GT | 979 |
| 11 | Guaymaral Airport |  | CO | 976 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 946 |
| 13 | El Dorado International Airport |  | CO | 926 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 864 |
| 15 | Chicago O'Hare International Airport |  | US | 828 |
| 16 | Madrid Barajas International Airport |  | ES | 783 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 739 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 715 |
| 20 | Malpensa International Airport |  | IT | 712 |
| 21 | Salt Lake City International Airport |  | US | 711 |
| 22 | Capua Airport |  | IT | 706 |
| 23 | Bengaluru International Airport |  | IN | 702 |
| 24 | Charles de Gaulle International Airport |  | FR | 670 |
| 25 | Charlotte/Douglas International Airport |  | US | 665 |
| 26 | Congonhas Airport |  | BR | 661 |
| 27 | Daniel K Inouye International Airport |  | US | 630 |
| 28 | Tenerife Norte Airport |  | ES | 629 |
| 29 | Ninoy Aquino International Airport |  | PH | 619 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 583 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 573 |
| 33 | Barcelona International Airport |  | ES | 573 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 553 |
| 35 | Vitoria/Foronda Airport |  | ES | 546 |
| 36 | Don Mueang International Airport |  | TH | 543 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 541 |
| 38 | Amsterdam Airport Schiphol |  | NL | 534 |
| 39 | O. R. Tambo International Airport |  | ZA | 508 |
| 40 | Calgary International Airport |  | CA | 502 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 405 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 319 | 21m | 244 km | 1,343.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 220 | 14m | 114 km | 431.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 180 | 26m | 275 km | 852.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 135 | 31m | 369 km | 859.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 128 | 27m | 152 km | 334.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 125 | 20m | 147 km | 316.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 109 | 1h 43m | 1,423 km | 2,675.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 109 | 18m | 144 km | 271.1 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 106 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 52m | 1,304 km | 2,339.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| D9730 |  | Schanis Airport (LSZX) | Bad Ragaz Airport (LSZE) | 2026-05-17 09:38 UTC | 2026-05-17 12:26 UTC | 2h 48m |
| N879MH |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-05-17 11:18 UTC | 2026-05-17 12:21 UTC | 1h 2m |
| N8323W |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-05-17 11:33 UTC | 2026-05-17 12:12 UTC | 39m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-16 21:36 UTC | 2026-05-17 12:08 UTC | 14h 31m |
| HK1479G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-17 11:39 UTC | 2026-05-17 12:05 UTC | 25m |
| N867MH |  | Nellis Afb Airport (KLSV) | Harry Reid International Airport (KLAS) | 2026-05-17 11:55 UTC | 2026-05-17 12:05 UTC | 9m |
| DEASO | DEA | Augsburg Airport (EDMA) | Friedrichshafen Airport (EDNY) | 2026-05-17 11:12 UTC | 2026-05-17 11:52 UTC | 40m |
| N3509A |  | 89LL (89LL) | 89LL (89LL) | 2026-05-17 11:45 UTC | 2026-05-17 11:51 UTC | 5m |
| N32CH |  | Livingston County/Spencer J Hardy Airport (KOZW) | Livingston County/Spencer J Hardy Airport (KOZW) | 2026-05-17 11:49 UTC | 2026-05-17 11:50 UTC | 0m |
| KLM71F | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Lauf-Lillinghof Airport (EDQI) | 2026-05-17 10:47 UTC | 2026-05-17 11:49 UTC | 1h 2m |
| FYG74YN | FYG | Rotterdam Airport (EHRD) | Rotterdam Airport (EHRD) | 2026-05-17 11:46 UTC | 2026-05-17 11:46 UTC | 0m |
| TRA8V | TRA | Amsterdam Airport Schiphol (EHAM) | Hoefen Airport (LOIR) | 2026-05-17 10:37 UTC | 2026-05-17 11:42 UTC | 1h 4m |
| HBZUL | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-05-17 10:28 UTC | 2026-05-17 11:39 UTC | 1h 11m |
| CPA331 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-17 04:21 UTC | 2026-05-17 11:38 UTC | 7h 17m |
| N816MH |  | Nellis Afb Airport (KLSV) | Harry Reid International Airport (KLAS) | 2026-05-17 11:27 UTC | 2026-05-17 11:36 UTC | 9m |
| AWA477 | AWA | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-05-17 10:54 UTC | 2026-05-17 11:35 UTC | 41m |
| N12180 |  | Stanton Airport (NY35) | Stanton Airport (NY35) | 2026-05-17 11:33 UTC | 2026-05-17 11:35 UTC | 2m |
| AFR78SW | Air France | Charles de Gaulle International Airport (LFPG) | Cannes-Mandelieu Airport (LFMD) | 2026-05-17 10:18 UTC | 2026-05-17 11:31 UTC | 1h 13m |
| KLM59J | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Słupsk-Krępa Airport (EPSR) | 2026-05-17 10:17 UTC | 2026-05-17 11:30 UTC | 1h 13m |
| AFR24JD | Air France | Charles de Gaulle International Airport (LFPG) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-05-17 10:36 UTC | 2026-05-17 11:30 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
