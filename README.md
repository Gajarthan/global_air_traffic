# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_15:19:27_UTC-green)

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

**Latest saved flight:** 2026-06-08 15:19:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-08 15:19:27 UTC

- **106,070** saved flights
- **37,281** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **106,070** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,297,302.7 tonnes** estimated CO2 emissions
- **75,205,952 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4381 |
| 2 | SkyWest Airlines | 3981 |
| 3 | IndiGo | 2110 |
| 4 | EJA | 2030 |
| 5 | American Airlines | 1697 |
| 6 | Southwest Airlines | 1598 |
| 7 | ENY | 1328 |
| 8 | Delta Air Lines | 1256 |
| 9 | Lufthansa | 1216 |
| 10 | Vueling | 974 |
| 11 | LATAM Airlines | 939 |
| 12 | WIF | 929 |
| 13 | AXM | 910 |
| 14 | AZU | 857 |
| 15 | LXJ | 799 |
| 16 | Swiss International | 773 |
| 17 | All Nippon Airways | 741 |
| 18 | Alaska Airlines | 732 |
| 19 | QLK | 710 |
| 20 | easyJet | 687 |
| 21 | EJU | 678 |
| 22 | Cathay Pacific | 633 |
| 23 | AEE | 611 |
| 24 | VIV | 606 |
| 25 | Air France | 605 |
| 26 | United Airlines | 586 |
| 27 | MXY | 578 |
| 28 | CXK | 559 |
| 29 | Japan Airlines | 526 |
| 30 | AXB | 521 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 89085 |
| 2 | 🇪🇸 ES | 7297 |
| 3 | 🇮🇳 IN | 6655 |
| 4 | 🇦🇺 AU | 6387 |
| 5 | 🇧🇷 BR | 5812 |
| 6 | 🇩🇪 DE | 5705 |
| 7 | 🇮🇹 IT | 5691 |
| 8 | 🇨🇦 CA | 5518 |
| 9 | 🇯🇵 JP | 4874 |
| 10 | 🇬🇧 GB | 4498 |
| 11 | 🇫🇷 FR | 4222 |
| 12 | 🇨🇴 CO | 3653 |
| 13 | 🇲🇽 MX | 3169 |
| 14 | 🇬🇷 GR | 3015 |
| 15 | 🇳🇴 NO | 2939 |
| 16 | 🇨🇭 CH | 2717 |
| 17 | 🇲🇾 MY | 2335 |
| 18 | 🇹🇷 TR | 2044 |
| 19 | 🇿🇦 ZA | 1834 |
| 20 | 🇰🇷 KR | 1773 |
| 21 | 🇳🇿 NZ | 1766 |
| 22 | 🇹🇭 TH | 1759 |
| 23 | 🇵🇱 PL | 1732 |
| 24 | 🇵🇭 PH | 1567 |
| 25 | 🇬🇹 GT | 1530 |
| 26 | 🇲🇦 MA | 1174 |
| 27 | 🇲🇴 MO | 1107 |
| 28 | 🇳🇱 NL | 1045 |
| 29 | 🇲🇪 ME | 1021 |
| 30 | 🇭🇷 HR | 926 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2297 |
| 2 | Denver International Airport |  | US | 1810 |
| 3 | Tokyo International Airport |  | JP | 1613 |
| 4 | Indira Gandhi International Airport |  | IN | 1447 |
| 5 | Harry Reid International Airport |  | US | 1355 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1337 |
| 7 | Guaymaral Airport |  | CO | 1332 |
| 8 | Zurich Airport |  | CH | 1205 |
| 9 | Frankfurt am Main International Airport |  | DE | 1204 |
| 10 | La Aurora Airport |  | GT | 1178 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1143 |
| 12 | El Dorado International Airport |  | CO | 1113 |
| 13 | Macau International Airport |  | MO | 1107 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1066 |
| 15 | Chicago O'Hare International Airport |  | US | 1064 |
| 16 | Madrid Barajas International Airport |  | ES | 928 |
| 17 | Kuala Lumpur International Airport |  | MY | 915 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 906 |
| 19 | Salt Lake City International Airport |  | US | 905 |
| 20 | Capua Airport |  | IT | 903 |
| 21 | Charlotte/Douglas International Airport |  | US | 823 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 814 |
| 23 | Charles de Gaulle International Airport |  | FR | 805 |
| 24 | Congonhas Airport |  | BR | 805 |
| 25 | Malpensa International Airport |  | IT | 796 |
| 26 | Bengaluru International Airport |  | IN | 796 |
| 27 | Daniel K Inouye International Airport |  | US | 721 |
| 28 | Ninoy Aquino International Airport |  | PH | 718 |
| 29 | Tenerife Norte Airport |  | ES | 718 |
| 30 | Barcelona International Airport |  | ES | 695 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 684 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 683 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 682 |
| 34 | Amsterdam Airport Schiphol |  | NL | 647 |
| 35 | Don Mueang International Airport |  | TH | 643 |
| 36 | Vitoria/Foronda Airport |  | ES | 636 |
| 37 | Calgary International Airport |  | CA | 626 |
| 38 | Seattle-Tacoma International Airport |  | US | 616 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 607 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 606 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 550 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 389 | 21m | 244 km | 1,638.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 284 | 24m | 225 km | 1,101.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 268 | 14m | 114 km | 525.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 260 | 1h 25m | 910 km | 4,080.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 245 | 1h 10m | 770 km | 3,254.6 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 213 | 26m | 275 km | 1,009.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 205 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 147 | 27m | 152 km | 384.2 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 142 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 139 | 18m | 144 km | 345.8 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 130 | 1h 1m | 695 km | 1,558.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 124 | 1h 43m | 1,423 km | 3,043.2 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 124 | 44m | 241 km | 515.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 119 | 1h 18m | 961 km | 1,972.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6235J |  | Las Cruces International Airport (KLRU) | Truth Or Consequences Municipal Airport (KTCS) | 2026-06-08 14:41 UTC | 2026-06-08 15:19 UTC | 37m |
| N20341 |  | Lea County Regional Airport (KHOB) | Lea County Regional Airport (KHOB) | 2026-06-08 14:57 UTC | 2026-06-08 15:13 UTC | 16m |
| UTA809 | UTA | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-06-08 07:20 UTC | 2026-06-08 15:12 UTC | 7h 52m |
| CXK669 | CXK | Raleigh-Durham International Airport (KRDU) | Raleigh Regional At Person County Airport (KTDF) | 2026-06-08 14:42 UTC | 2026-06-08 15:12 UTC | 30m |
| N914SW |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-06-08 14:38 UTC | 2026-06-08 15:11 UTC | 32m |
| BOMR806 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-06-08 14:43 UTC | 2026-06-08 15:05 UTC | 22m |
| MANLY51 | MAN | Lariat Ranch Airport (OK42) | Lariat Ranch Airport (OK42) | 2026-06-08 14:48 UTC | 2026-06-08 15:05 UTC | 16m |
| TGTJH | TGT | Matehuala Airport (MM67) | Muzquiz New Airport (MM42) | 2026-06-08 12:57 UTC | 2026-06-08 15:04 UTC | 2h 7m |
| N115PJ |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-06-08 14:30 UTC | 2026-06-08 15:03 UTC | 33m |
| RYR52SU | Ryanair | Treviso / Sant'Angelo Airport (LIPH) | Teruel Airport (LETL) | 2026-06-08 13:11 UTC | 2026-06-08 14:59 UTC | 1h 48m |
| N257EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-08 14:09 UTC | 2026-06-08 14:57 UTC | 48m |
| DUKE40 | DUK | Wiesbaden Army Airfield (ETOU) | Stuttgart Airport (EDDS) | 2026-06-08 12:55 UTC | 2026-06-08 14:53 UTC | 1h 57m |
| PTZNG | PTZ | Marchesan S.A. Airport (SDME) | Eurico de Aguiar Salles Airport (SBVT) | 2026-06-08 13:39 UTC | 2026-06-08 14:52 UTC | 1h 12m |
| RNGR743 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Victoria Regional Airport (KVCT) | 2026-06-08 14:24 UTC | 2026-06-08 14:52 UTC | 27m |
| SWR4KW | Swiss International | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 2026-06-08 13:46 UTC | 2026-06-08 14:51 UTC | 1h 5m |
| N593WT |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Wichita Dwight D Eisenhower Ntl Airport (KICT) | 2026-06-08 13:48 UTC | 2026-06-08 14:49 UTC | 1h 1m |
| MANLY51 | MAN | Enix Airport (OK51) | Lariat Ranch Airport (OK42) | 2026-06-08 14:09 UTC | 2026-06-08 14:48 UTC | 39m |
| N637W |  | Lake Havasu City Airport (KHII) | Colorado Plains Regional Airport (KAKO) | 2026-06-08 13:13 UTC | 2026-06-08 14:47 UTC | 1h 33m |
| N96HE |  | Stoneriver Airport (NC09) | Weaver Field (SC94) | 2026-06-08 14:14 UTC | 2026-06-08 14:47 UTC | 32m |
| HBZPV | HBZ | Sion Airport (LSGS) | Muenster Aero Airport (LSPU) | 2026-06-08 12:26 UTC | 2026-06-08 14:46 UTC | 2h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
