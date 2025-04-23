from typing import List

from sqlmodel import SQLModel, Field, Relationship

class Switch(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    ip: str = Field(index=True, max_length=15)
    vlans: List["Vlan"] = Relationship(back_populates="switch")
    ports: List["Port"] = Relationship(back_populates="switch")


class Vlan(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    num: int = Field(index=True)
    switch_id: int = Field(foreign_key="switch.id")
    switch: Switch | None = Relationship(back_populates="vlans")
    ports: List["Port"] = Relationship(back_populates="vlan")


class Port(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    switch_id: int = Field(foreign_key="switch.id")
    vlan_id: int = Field(foreign_key="vlan.id")
    switch: Switch | None = Relationship(back_populates="ports")
    vlan: Vlan | None = Relationship(back_populates="ports")