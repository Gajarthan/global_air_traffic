# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_17:05:51_UTC-green)

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

**Latest saved flight:** 2026-05-21 17:05:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 17:05:51 UTC

- **90,283** saved flights
- **32,127** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **90,283** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,115,448.5 tonnes** estimated CO2 emissions
- **64,663,680 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3866 |
| 2 | SkyWest Airlines | 3341 |
| 3 | IndiGo | 1898 |
| 4 | EJA | 1705 |
| 5 | American Airlines | 1374 |
| 6 | Southwest Airlines | 1306 |
| 7 | Lufthansa | 1119 |
| 8 | ENY | 1110 |
| 9 | Delta Air Lines | 990 |
| 10 | Vueling | 860 |
| 11 | LATAM Airlines | 815 |
| 12 | AXM | 800 |
| 13 | WIF | 793 |
| 14 | AZU | 716 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 679 |
| 17 | LXJ | 672 |
| 18 | Alaska Airlines | 639 |
| 19 | QLK | 639 |
| 20 | easyJet | 592 |
| 21 | EJU | 581 |
| 22 | Cathay Pacific | 579 |
| 23 | AEE | 554 |
| 24 | VIV | 536 |
| 25 | Air France | 531 |
| 26 | Japan Airlines | 482 |
| 27 | CXK | 474 |
| 28 | AXB | 462 |
| 29 | MXY | 461 |
| 30 | AIQ | 437 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 74269 |
| 2 | 🇪🇸 ES | 6407 |
| 3 | 🇮🇳 IN | 5968 |
| 4 | 🇦🇺 AU | 5618 |
| 5 | 🇩🇪 DE | 4989 |
| 6 | 🇮🇹 IT | 4977 |
| 7 | 🇧🇷 BR | 4952 |
| 8 | 🇨🇦 CA | 4526 |
| 9 | 🇯🇵 JP | 4400 |
| 10 | 🇬🇧 GB | 3862 |
| 11 | 🇫🇷 FR | 3633 |
| 12 | 🇨🇴 CO | 3111 |
| 13 | 🇲🇽 MX | 2782 |
| 14 | 🇬🇷 GR | 2597 |
| 15 | 🇳🇴 NO | 2531 |
| 16 | 🇨🇭 CH | 2376 |
| 17 | 🇲🇾 MY | 2011 |
| 18 | 🇹🇷 TR | 1648 |
| 19 | 🇿🇦 ZA | 1645 |
| 20 | 🇳🇿 NZ | 1555 |
| 21 | 🇹🇭 TH | 1537 |
| 22 | 🇵🇱 PL | 1489 |
| 23 | 🇰🇷 KR | 1417 |
| 24 | 🇵🇭 PH | 1387 |
| 25 | 🇬🇹 GT | 1350 |
| 26 | 🇲🇦 MA | 1044 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇲🇪 ME | 919 |
| 29 | 🇳🇱 NL | 917 |
| 30 | 🇭🇷 HR | 820 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1970 |
| 2 | Denver International Airport |  | US | 1511 |
| 3 | Tokyo International Airport |  | JP | 1468 |
| 4 | Indira Gandhi International Airport |  | IN | 1294 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1221 |
| 6 | Harry Reid International Airport |  | US | 1155 |
| 7 | Frankfurt am Main International Airport |  | DE | 1128 |
| 8 | Guaymaral Airport |  | CO | 1073 |
| 9 | Zurich Airport |  | CH | 1069 |
| 10 | Macau International Airport |  | MO | 1035 |
| 11 | La Aurora Airport |  | GT | 1030 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 994 |
| 13 | El Dorado International Airport |  | CO | 983 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 915 |
| 15 | Chicago O'Hare International Airport |  | US | 869 |
| 16 | Madrid Barajas International Airport |  | ES | 819 |
| 17 | Kuala Lumpur International Airport |  | MY | 796 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 772 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 759 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 733 |
| 22 | Malpensa International Airport |  | IT | 729 |
| 23 | Bengaluru International Airport |  | IN | 717 |
| 24 | Charles de Gaulle International Airport |  | FR | 707 |
| 25 | Charlotte/Douglas International Airport |  | US | 693 |
| 26 | Congonhas Airport |  | BR | 693 |
| 27 | Tenerife Norte Airport |  | ES | 660 |
| 28 | Daniel K Inouye International Airport |  | US | 659 |
| 29 | Ninoy Aquino International Airport |  | PH | 637 |
| 30 | Barcelona International Airport |  | ES | 609 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 600 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 593 |
| 34 | Vitoria/Foronda Airport |  | ES | 572 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 570 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Don Mueang International Airport |  | TH | 564 |
| 38 | Amsterdam Airport Schiphol |  | NL | 562 |
| 39 | Calgary International Airport |  | CA | 535 |
| 40 | O. R. Tambo International Airport |  | ZA | 520 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 439 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 335 | 21m | 244 km | 1,410.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 249 | 24m | 225 km | 966.0 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 235 | 14m | 114 km | 460.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 234 | 9m | - | - |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 232 | 1h 26m | 910 km | 3,640.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 231 | 28m | 304 km | 1,211.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 208 | 1h 10m | 770 km | 2,763.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 196 | 19m | 165 km | 557.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 186 | 26m | 275 km | 881.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 135 | 27m | 215 km | 500.0 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 134 | 23m | 55 km | 127.4 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 129 | 14m | 154 km | 341.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 117 | 18m | 144 km | 291.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 110 | 1h 40m | 1,156 km | 2,194.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CONGO65 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-05-21 16:34 UTC | 2026-05-21 17:05 UTC | 31m |
| N331RF |  | Leoville Airport (CJT9) | Leoville Airport (CJT9) | 2026-05-21 16:41 UTC | 2026-05-21 17:02 UTC | 21m |
| N631SA |  | Falcon Field (KFFZ) | Rimrock Airport (48AZ) | 2026-05-21 16:26 UTC | 2026-05-21 16:55 UTC | 28m |
| LAE1828 | LAE | Los Angeles International Airport (KLAX) | Seattle-Tacoma International Airport (KSEA) | 2026-05-21 14:23 UTC | 2026-05-21 16:51 UTC | 2h 27m |
| N12541 |  | Pittsburgh/Butler Regional Airport (KBTP) | Pittsburgh/Butler Regional Airport (KBTP) | 2026-05-21 15:56 UTC | 2026-05-21 16:50 UTC | 54m |
| OXF6250 | OXF | Falcon Field (KFFZ) | 2AZ8 (2AZ8) | 2026-05-21 15:16 UTC | 2026-05-21 16:49 UTC | 1h 32m |
| N285PJ |  | Kern Valley Airport (KL05) | Sequoia Ranch Airport (CA44) | 2026-05-21 16:30 UTC | 2026-05-21 16:45 UTC | 14m |
| N91XA |  | Wiita Farms Airport (65OH) | Canal Fulton Airport (7OH2) | 2026-05-21 16:20 UTC | 2026-05-21 16:45 UTC | 24m |
| FHGTJ | FHG | Aix-en-Provence (BA 114) Airport (LFMA) | Nimes-Arles-Camargue Airport (LFTW) | 2026-05-21 16:04 UTC | 2026-05-21 16:43 UTC | 38m |
| VAR496 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-21 15:42 UTC | 2026-05-21 16:42 UTC | 1h 0m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-05-21 16:33 UTC | 2026-05-21 16:42 UTC | 9m |
| N139XL |  | Austin-Bergstrom International Airport (KAUS) | Addison Airport (KADS) | 2026-05-21 15:53 UTC | 2026-05-21 16:37 UTC | 44m |
| N9565J |  | French Valley Airport (KF70) | Big Bear City Airport (KL35) | 2026-05-21 15:29 UTC | 2026-05-21 16:35 UTC | 1h 5m |
| N526ZK |  | Palo Alto Airport (KPAO) | Hayward Executive Airport (KHWD) | 2026-05-21 15:27 UTC | 2026-05-21 16:33 UTC | 1h 6m |
| N3049Q |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-05-21 16:16 UTC | 2026-05-21 16:31 UTC | 15m |
| ERU98 | ERU | Cottonwood Airport (KP52) | Cottonwood Airport (KP52) | 2026-05-20 23:44 UTC | 2026-05-21 16:31 UTC | 16h 46m |
| N472LJ |  | Scottsdale Airport (KSDL) | Sedona Airport (KSEZ) | 2026-05-21 16:10 UTC | 2026-05-21 16:29 UTC | 19m |
| WAH | WAH | Beluga Airport (PABG) | Nikolai Creek Airport (9AK3) | 2026-05-21 16:18 UTC | 2026-05-21 16:28 UTC | 10m |
| N118UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-05-21 16:06 UTC | 2026-05-21 16:27 UTC | 21m |
| HK5431G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-21 16:05 UTC | 2026-05-21 16:27 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
