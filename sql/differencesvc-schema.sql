
CREATE TABLE difference_requests
(
    id INTEGER ,
    n INTEGER NOT NULL ,
    created INTEGER NOT NULL ,
    occurrences INTEGER NOT NULL ,
    PRIMARY KEY (id ASC)
);

CREATE INDEX idx_n ON difference_requests(n);

