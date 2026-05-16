# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_10:16:39_UTC-green)

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

**Latest saved flight:** 2026-05-16 10:16:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 10:16:39 UTC

- **84,448** saved flights
- **30,417** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,448** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,041,547.6 tonnes** estimated CO2 emissions
- **60,379,570 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3610 |
| 2 | SkyWest Airlines | 3127 |
| 3 | IndiGo | 1825 |
| 4 | EJA | 1594 |
| 5 | American Airlines | 1300 |
| 6 | Southwest Airlines | 1238 |
| 7 | Lufthansa | 1071 |
| 8 | ENY | 1053 |
| 9 | Delta Air Lines | 922 |
| 10 | Vueling | 798 |
| 11 | AXM | 766 |
| 12 | LATAM Airlines | 764 |
| 13 | WIF | 730 |
| 14 | AZU | 661 |
| 15 | All Nippon Airways | 657 |
| 16 | Swiss International | 656 |
| 17 | QLK | 620 |
| 18 | LXJ | 619 |
| 19 | Alaska Airlines | 599 |
| 20 | easyJet | 555 |
| 21 | EJU | 537 |
| 22 | AEE | 533 |
| 23 | Cathay Pacific | 531 |
| 24 | VIV | 505 |
| 25 | Air France | 495 |
| 26 | Japan Airlines | 474 |
| 27 | AXB | 448 |
| 28 | CXK | 446 |
| 29 | MXY | 420 |
| 30 | United Airlines | 417 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69191 |
| 2 | 🇪🇸 ES | 5962 |
| 3 | 🇮🇳 IN | 5714 |
| 4 | 🇦🇺 AU | 5410 |
| 5 | 🇩🇪 DE | 4690 |
| 6 | 🇮🇹 IT | 4650 |
| 7 | 🇧🇷 BR | 4643 |
| 8 | 🇯🇵 JP | 4252 |
| 9 | 🇨🇦 CA | 4203 |
| 10 | 🇬🇧 GB | 3598 |
| 11 | 🇫🇷 FR | 3347 |
| 12 | 🇨🇴 CO | 2821 |
| 13 | 🇲🇽 MX | 2566 |
| 14 | 🇬🇷 GR | 2455 |
| 15 | 🇳🇴 NO | 2354 |
| 16 | 🇨🇭 CH | 2229 |
| 17 | 🇲🇾 MY | 1920 |
| 18 | 🇿🇦 ZA | 1590 |
| 19 | 🇹🇷 TR | 1501 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1466 |
| 22 | 🇵🇱 PL | 1400 |
| 23 | 🇵🇭 PH | 1324 |
| 24 | 🇰🇷 KR | 1305 |
| 25 | 🇬🇹 GT | 1272 |
| 26 | 🇲🇦 MA | 979 |
| 27 | 🇲🇴 MO | 978 |
| 28 | 🇲🇪 ME | 887 |
| 29 | 🇳🇱 NL | 861 |
| 30 | 🇭🇷 HR | 754 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1849 |
| 2 | Tokyo International Airport |  | JP | 1421 |
| 3 | Denver International Airport |  | US | 1419 |
| 4 | Indira Gandhi International Airport |  | IN | 1218 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1186 |
| 6 | Frankfurt am Main International Airport |  | DE | 1086 |
| 7 | Harry Reid International Airport |  | US | 1061 |
| 8 | Zurich Airport |  | CH | 1004 |
| 9 | Macau International Airport |  | MO | 978 |
| 10 | La Aurora Airport |  | GT | 965 |
| 11 | Guaymaral Airport |  | CO | 948 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 909 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 850 |
| 15 | Chicago O'Hare International Airport |  | US | 816 |
| 16 | Madrid Barajas International Airport |  | ES | 769 |
| 17 | Kuala Lumpur International Airport |  | MY | 763 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 728 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 706 |
| 20 | Salt Lake City International Airport |  | US | 704 |
| 21 | Malpensa International Airport |  | IT | 704 |
| 22 | Bengaluru International Airport |  | IN | 698 |
| 23 | Capua Airport |  | IT | 687 |
| 24 | Charles de Gaulle International Airport |  | FR | 660 |
| 25 | Charlotte/Douglas International Airport |  | US | 656 |
| 26 | Congonhas Airport |  | BR | 656 |
| 27 | Daniel K Inouye International Airport |  | US | 615 |
| 28 | Tenerife Norte Airport |  | ES | 610 |
| 29 | Ninoy Aquino International Airport |  | PH | 606 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 570 |
| 32 | Barcelona International Airport |  | ES | 563 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 562 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 542 |
| 35 | Vitoria/Foronda Airport |  | ES | 533 |
| 36 | Don Mueang International Airport |  | TH | 530 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 530 |
| 38 | Amsterdam Airport Schiphol |  | NL | 522 |
| 39 | O. R. Tambo International Airport |  | ZA | 501 |
| 40 | Calgary International Airport |  | CA | 494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 312 | 21m | 244 km | 1,313.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 275 | 1h 7m | 706 km | 3,348.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 224 | 28m | 304 km | 1,174.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 217 | 14m | 114 km | 425.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 192 | 1h 11m | 770 km | 2,550.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 190 | 19m | 165 km | 540.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 177 | 26m | 275 km | 838.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 143 | 20m | 99 km | 244.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 131 | 31m | 369 km | 833.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 126 | 27m | 152 km | 329.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 121 | 14m | 154 km | 320.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 119 | 23m | 55 km | 113.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 107 | 18m | 144 km | 266.2 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-05-16 10:05 UTC | 2026-05-16 10:16 UTC | 10m |
| SXARH | SXA | Megara Airport (LGMG) | Milos Airport (LGML) | 2026-05-16 08:34 UTC | 2026-05-16 10:05 UTC | 1h 31m |
| N815MH |  | Nellis Afb Airport (KLSV) | Harry Reid International Airport (KLAS) | 2026-05-16 09:46 UTC | 2026-05-16 09:57 UTC | 11m |
| RNA409 | RNA | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-05-16 06:13 UTC | 2026-05-16 09:56 UTC | 3h 43m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-15 22:16 UTC | 2026-05-16 09:53 UTC | 11h 37m |
| SWR3AV | Swiss International | Manchester Airport (EGCC) | Zurich Airport (LSZH) | 2026-05-16 08:24 UTC | 2026-05-16 09:53 UTC | 1h 28m |
| ECOAIR21 | ECO | Blaise Diagne International Airport (GOBD) | Blaise Diagne International Airport (GOBD) | 2026-05-16 08:10 UTC | 2026-05-16 09:48 UTC | 1h 38m |
| CPA565 | Cathay Pacific | Kansai International Airport (RJBB) | Longtan Air Base (RCDI) | 2026-05-16 07:38 UTC | 2026-05-16 09:47 UTC | 2h 8m |
| UBA2585 | UBA | Mano Dayak International Airport (DRZA) | Anisakan Airport (VYAS) | 2026-05-16 00:00 UTC | 2026-05-16 09:43 UTC | 9h 42m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Molde Airport (ENML) | 2026-05-16 08:56 UTC | 2026-05-16 09:35 UTC | 38m |
| TBJ31 | TBJ | Tbilisi International Airport (UGTB) | Macau International Airport (VMMC) | 2026-05-16 01:26 UTC | 2026-05-16 09:34 UTC | 8h 8m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-05-16 09:08 UTC | 2026-05-16 09:34 UTC | 25m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Reykholar Airport (BIRE) | 2026-05-16 09:13 UTC | 2026-05-16 09:32 UTC | 19m |
| IGO941 | IndiGo | Yelahanka Air Force Station (VOYK) | Gwalior Airport (VIGR) | 2026-05-16 07:45 UTC | 2026-05-16 09:32 UTC | 1h 46m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-05-15 22:18 UTC | 2026-05-16 09:30 UTC | 11h 12m |
| IGO7313 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Lokpriya Gopinath Bordoloi International Airport (VEGT) | 2026-05-16 08:14 UTC | 2026-05-16 09:29 UTC | 1h 15m |
| DEBWF | DEB | Bonn-Hangelar Airport (EDKB) | Bad Neuenahr-Ahrweiler Airport (EDRA) | 2026-05-16 09:14 UTC | 2026-05-16 09:26 UTC | 12m |
| JL3555 |  | Fukuoka Airport (RJFF) | Hiroshima Airport (RJOA) | 2026-05-16 08:44 UTC | 2026-05-16 09:26 UTC | 41m |
| SWR5ZM | Swiss International | Zurich Airport (LSZH) | Stockholm-Arlanda Airport (ESSA) | 2026-05-16 07:18 UTC | 2026-05-16 09:25 UTC | 2h 7m |
| IGO502F | IndiGo | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-05-16 08:58 UTC | 2026-05-16 09:24 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
