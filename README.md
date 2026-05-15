# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_07:27:34_UTC-green)

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

**Latest saved flight:** 2026-05-15 07:27:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 07:27:34 UTC

- **82,738** saved flights
- **29,954** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **82,738** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,019,200.8 tonnes** estimated CO2 emissions
- **59,084,107 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3540 |
| 2 | SkyWest Airlines | 3066 |
| 3 | IndiGo | 1803 |
| 4 | EJA | 1554 |
| 5 | American Airlines | 1277 |
| 6 | Southwest Airlines | 1211 |
| 7 | Lufthansa | 1065 |
| 8 | ENY | 1034 |
| 9 | Delta Air Lines | 906 |
| 10 | Vueling | 784 |
| 11 | LATAM Airlines | 752 |
| 12 | AXM | 749 |
| 13 | WIF | 716 |
| 14 | AZU | 653 |
| 15 | All Nippon Airways | 649 |
| 16 | Swiss International | 641 |
| 17 | QLK | 614 |
| 18 | LXJ | 601 |
| 19 | Alaska Airlines | 587 |
| 20 | easyJet | 546 |
| 21 | EJU | 530 |
| 22 | AEE | 524 |
| 23 | Cathay Pacific | 518 |
| 24 | VIV | 494 |
| 25 | Air France | 484 |
| 26 | Japan Airlines | 467 |
| 27 | AXB | 442 |
| 28 | CXK | 432 |
| 29 | MXY | 410 |
| 30 | AIQ | 409 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 67655 |
| 2 | 🇪🇸 ES | 5852 |
| 3 | 🇮🇳 IN | 5635 |
| 4 | 🇦🇺 AU | 5304 |
| 5 | 🇩🇪 DE | 4632 |
| 6 | 🇧🇷 BR | 4580 |
| 7 | 🇮🇹 IT | 4564 |
| 8 | 🇯🇵 JP | 4186 |
| 9 | 🇨🇦 CA | 4122 |
| 10 | 🇬🇧 GB | 3522 |
| 11 | 🇫🇷 FR | 3284 |
| 12 | 🇨🇴 CO | 2756 |
| 13 | 🇲🇽 MX | 2506 |
| 14 | 🇬🇷 GR | 2401 |
| 15 | 🇳🇴 NO | 2308 |
| 16 | 🇨🇭 CH | 2205 |
| 17 | 🇲🇾 MY | 1881 |
| 18 | 🇿🇦 ZA | 1556 |
| 19 | 🇹🇷 TR | 1466 |
| 20 | 🇳🇿 NZ | 1463 |
| 21 | 🇹🇭 TH | 1448 |
| 22 | 🇵🇱 PL | 1377 |
| 23 | 🇵🇭 PH | 1304 |
| 24 | 🇰🇷 KR | 1268 |
| 25 | 🇬🇹 GT | 1256 |
| 26 | 🇲🇦 MA | 962 |
| 27 | 🇲🇴 MO | 946 |
| 28 | 🇲🇪 ME | 880 |
| 29 | 🇳🇱 NL | 853 |
| 30 | 🇭🇷 HR | 736 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1822 |
| 2 | Tokyo International Airport |  | JP | 1403 |
| 3 | Denver International Airport |  | US | 1388 |
| 4 | Indira Gandhi International Airport |  | IN | 1196 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1172 |
| 6 | Frankfurt am Main International Airport |  | DE | 1076 |
| 7 | Harry Reid International Airport |  | US | 1033 |
| 8 | Zurich Airport |  | CH | 982 |
| 9 | La Aurora Airport |  | GT | 951 |
| 10 | Macau International Airport |  | MO | 946 |
| 11 | Guaymaral Airport |  | CO | 925 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 923 |
| 13 | El Dorado International Airport |  | CO | 889 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 829 |
| 15 | Chicago O'Hare International Airport |  | US | 803 |
| 16 | Madrid Barajas International Airport |  | ES | 754 |
| 17 | Kuala Lumpur International Airport |  | MY | 749 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 720 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 696 |
| 20 | Malpensa International Airport |  | IT | 695 |
| 21 | Bengaluru International Airport |  | IN | 693 |
| 22 | Salt Lake City International Airport |  | US | 684 |
| 23 | Capua Airport |  | IT | 675 |
| 24 | Charles de Gaulle International Airport |  | FR | 646 |
| 25 | Charlotte/Douglas International Airport |  | US | 645 |
| 26 | Congonhas Airport |  | BR | 643 |
| 27 | Daniel K Inouye International Airport |  | US | 601 |
| 28 | Tenerife Norte Airport |  | ES | 600 |
| 29 | Ninoy Aquino International Airport |  | PH | 597 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 588 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 555 |
| 32 | Barcelona International Airport |  | ES | 555 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 554 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 534 |
| 35 | Don Mueang International Airport |  | TH | 522 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 520 |
| 37 | Vitoria/Foronda Airport |  | ES | 519 |
| 38 | Amsterdam Airport Schiphol |  | NL | 515 |
| 39 | O. R. Tambo International Airport |  | ZA | 490 |
| 40 | Calgary International Airport |  | CA | 485 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 385 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 299 | 21m | 244 km | 1,259.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 221 | 28m | 304 km | 1,158.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 212 | 14m | 114 km | 415.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 196 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 187 | 1h 11m | 770 km | 2,484.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 172 | 26m | 275 km | 815.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 138 | 44m | 452 km | 1,075.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 124 | 27m | 152 km | 324.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 123 | 27m | 215 km | 455.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 121 | 20m | 147 km | 306.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 115 | 23m | 55 km | 109.3 t |
| 22 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 113 | 1h 2m | 695 km | 1,354.5 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 104 | 13m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 104 | 18m | 144 km | 258.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAE9869 | Emirates | Taiwan Taoyuan International Airport (RCTP) | Queen Alia International Airport (OJAI) | 2026-05-14 13:43 UTC | 2026-05-15 07:27 UTC | 17h 44m |
| IGT1166 | IGT | Tbilisi International Airport (UGTB) | Queen Alia International Airport (OJAI) | 2026-05-15 05:20 UTC | 2026-05-15 07:15 UTC | 1h 54m |
| UAE9852 | Emirates | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-05-14 15:01 UTC | 2026-05-15 07:12 UTC | 16h 10m |
| UAE56W | Emirates | Al Ain International Airport (OMAL) | Queen Alia International Airport (OJAI) | 2026-05-15 03:58 UTC | 2026-05-15 07:08 UTC | 3h 9m |
| QFA536 | Qantas | Sydney Kingsford Smith International Airport (YSSY) | Dunwich Airport (YDUN) | 2026-05-15 05:47 UTC | 2026-05-15 07:07 UTC | 1h 20m |
| EJU73DN | EJU | Amsterdam Airport Schiphol (EHAM) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-15 05:34 UTC | 2026-05-15 07:05 UTC | 1h 31m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-05-14 20:14 UTC | 2026-05-15 07:02 UTC | 10h 47m |
| ICL7674 | ICL | Indira Gandhi International Airport (VIDP) | Jallowal Airport (VI88) | 2026-05-15 06:27 UTC | 2026-05-15 07:02 UTC | 35m |
| SDA266 | SDA | Paraparaumu Airport (NZPP) | Wellington International Airport (NZWN) | 2026-05-15 06:47 UTC | 2026-05-15 07:02 UTC | 14m |
| N544SF |  | Skypark Airport (KBTF) | Wendover Airport (KENV) | 2026-05-15 05:50 UTC | 2026-05-15 06:58 UTC | 1h 7m |
| ZUTSI | ZUT | Tedderfield Air Park (FATA) | Lanseria Airport (FALA) | 2026-05-15 06:43 UTC | 2026-05-15 06:52 UTC | 8m |
| IGO497W | IndiGo | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-15 04:56 UTC | 2026-05-15 06:46 UTC | 1h 49m |
|  |  | Rzeszow-Jasionka Airport (EPRZ) | Rzeszów Airport (EPRJ) | 2026-05-15 06:37 UTC | 2026-05-15 06:39 UTC | 2m |
| N34RF |  | City Of Colorado Springs Municipal Airport (KCOS) | Indianapolis Metro Airport (KUMP) | 2026-05-15 03:21 UTC | 2026-05-15 06:38 UTC | 3h 17m |
| EWG4R | EWG | Cologne Bonn Airport (EDDK) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-15 05:12 UTC | 2026-05-15 06:37 UTC | 1h 25m |
| RYR791X | Ryanair | Ciampino Airport (LIRA) | London Stansted Airport (EGSS) | 2026-05-15 04:27 UTC | 2026-05-15 06:36 UTC | 2h 9m |
| OKPHS | OKP | Kunovice Airport (LKKU) | Václav Havel Airport (LKPR) | 2026-05-15 05:59 UTC | 2026-05-15 06:36 UTC | 36m |
| UPS2 | UPS | Cologne Bonn Airport (EDDK) | Macau International Airport (VMMC) | 2026-05-14 19:19 UTC | 2026-05-15 06:36 UTC | 11h 16m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-05-15 05:14 UTC | 2026-05-15 06:33 UTC | 1h 19m |
| RYR2ZL | Ryanair | Alicante International Airport (LEAL) | Belfast International Airport (EGAA) | 2026-05-15 03:51 UTC | 2026-05-15 06:31 UTC | 2h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
